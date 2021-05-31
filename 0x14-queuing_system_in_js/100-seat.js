/* Create client */
const client = require("redis").createClient()
import { promisify } from 'util'
const getAsync = promisify(client.get).bind(client)

client.on("connect", () => {
  console.log("Redis client connected to the server")
  reserveSeat(50)
})

client.on("error", error => {
  console.log(`Redis client not connected to the server: ${error}`)
})

const reserveSeat = number => client.set("available_seats", number)

const getCurrentAvailableSeats = async () => await getAsync("available_seats")

let reservationEnabled = true

/* Create queue */
const queue = require("kue").createQueue()

/* Create server */
const express = require("express")
const app = express()
const port = 1245

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats()
  res.json({ numberOfAvailableSeats: availableSeats })
})

app.get('/reserve_seat', (req, res) => {
  if (reservationEnabled) {
    const job = queue.create('reserve_seat')
      .save(err => {
        err ?
          res.json({ "status": "Reservation failed" }) :
          res.json({ "status": "Reservation in process" })
      })

    job
      .on("complete", result => {
        console.log(`Seat reservation job ${job.id} completed`)
      })
      .on("failed", errorMessage => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`)
      })
  } else {
    res.json({ "status": "Reservation are blocked" })
  }
})

app.get('/process', (req, res) => {
  queue.process("reserve_seat", async (job, done) => {
    try {
      const availableSeats = await getCurrentAvailableSeats()
      if (availableSeats > 0) {
        await reserveSeat(availableSeats - 1)
        if ((availableSeats - 1) === 0) reservationEnabled = false
      }

      if ((availableSeats - 1) >= 0) {
        done()
      } else {
        return done(Error("Not enough seats available"))
      }
    } catch (error) {
      console.log(error.message)
    }
  })
  res.json({ "status": "Queue processing" })
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))
