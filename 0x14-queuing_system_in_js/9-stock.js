const express = require('express');
const app = express();
const port = 1245;

const client = require('redis').createClient();
import { promisify } from 'util'
const getAsync = promisify(client.get).bind(client)
const setAsync = promisify(client.set).bind(client)

client.on("connect", () => {
  console.log("Redis client connected to the server")
})

client.on("error", error => {
  console.log(`Redis client not connected to the server: ${error}`)
})

const listProducts = [
  { "itemId": 1, "itemName": "Suitcase 250", "price": 50, "initialAvailableQuantity": 4 },
  { "itemId": 2, "itemName": "Suitcase 450", "price": 100, "initialAvailableQuantity": 10 },
  { "itemId": 3, "itemName": "Suitcase 650", "price": 350, "initialAvailableQuantity": 2 },
  { "itemId": 4, "itemName": "Suitcase 1050", "price": 550, "initialAvailableQuantity": 5 }
]

const getItemById = id => {
  for (const item of listProducts) {
    if (item.itemId === id) return item
  }
}

app.get('/list_products', (req, res) => res.json(listProducts))

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params
  const inStock = getItemById(parseInt(itemId))
  const reserved = await getCurrentReservedStockById(parseInt(itemId))
  if (inStock) {
    if (reserved) {
      inStock.currentQuantity = reserved
    } else {
      inStock.currentQuantity = inStock.initialAvailableQuantity
      await reserveStockById(itemId, inStock.initialAvailableQuantity)
    }
    res.json(inStock)
  } else {
    res.json({ "status": "Product not found" })
  }
})

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params
  const inStock = getItemById(parseInt(itemId))
  const reserved = await getCurrentReservedStockById(parseInt(itemId))
  if (!inStock) res.json({ "status": "Product not found" })

  if (!reserved || reserved > 0) {
    inStock.initialAvailableQuantity -= 1
    inStock.currentQuantity = inStock.initialAvailableQuantity
    await reserveStockById(itemId, inStock.initialAvailableQuantity)
    res.json({ "status": "Reservation confirmed", "itemId": `${itemId}` })
  } else if (reserved < 1) {
    res.json({ "status": "Not enough stock available", "itemId": `${itemId}` })
  }
})

app.listen(port)

const reserveStockById = async (itemId, stock) => await setAsync(itemId, stock)

const getCurrentReservedStockById = async (itemId) => await getAsync(itemId)

module.exports = app;
