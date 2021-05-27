const express = require('express')
const app = express()
const port = 7865

app.get('/', (req, res) => {
  res.status(200)
  res.send('Welcome to the payment system')
})

app.get('/cart/:id', (req, res) => {
  const { id } = req.params

  if (typeof (parseInt(id)) === 'number') {
    res.status(200)
    res.send(`Payment methods for cart ${id}`)
  } else {
    res.status(404)
    res.send("Not a number")
  }
})

app.listen(port, () => {
  console.log(`API available on localhost port 7865`)
})
