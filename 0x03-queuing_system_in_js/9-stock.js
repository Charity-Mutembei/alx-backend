/* eslint-disable no-ternary */
/* eslint-disable multiline-ternary */
/* eslint-disable sort-vars */
/* eslint-disable no-undef */
/* eslint-disable no-magic-numbers */
/* eslint-disable sort-keys */
/* eslint-disable one-var */
// /* eslint-disable no-unused-vars */
// /* eslint-disable sort-keys */
// Const listProducts = [
//     {
//         'itemId': 1,
//         'itemName': 'Suitcase 250',
//         'price': 50,
//         'initialAvailableQuantity': 4
//     },
//     {
//         'itemId': 2,
//         'itemName': 'Suitcase 450',
//         'price': 100,
//         'initialAvailableQuantity': 10
//     },
//     {
//         'itemId': 3,
//         'itemName': 'Suitcase 650',
//         'price': 350,
//         'initialAvailableQuantity': 2
//     },
//     {
//         'itemId': 4,
//         'itemName': 'Suitcase 1050',
//         'price': 550,
//         'initialAvailableQuantity': 5
//     }
//   ];

import express from 'express';
import {promisify} from 'util';
import redis from 'redis';

const app = express(),
 port = 1245,

// Redis client setup
 redisClient = redis.createClient(),
 getAsync = promisify(redisClient.get).bind(redisClient),
 setAsync = promisify(redisClient.set).bind(redisClient),

// Function to reserve stock in Redis
 reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock.toString());
},

// Function to get current reserved stock from Redis
 getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);


return stock ? parseInt(stock, 10) : 0;
},

// Function to get product details by itemId
 getItemById = (id) => listProducts.find((product) => product.itemId === id);

// Route to get list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    'itemId': product.itemId,
    'itemName': product.itemName,
    'price': product.price,
    'initialAvailableQuantity': product.initialAvailableQuantity
  })));
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10),
   product = getItemById(itemId);

  if (!product) {
    res.json({'status': 'Product not found'});

return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  res.json({
    'itemId': product.itemId,
    'itemName': product.itemName,
    'price': product.price,
    'initialAvailableQuantity': product.initialAvailableQuantity,
    currentQuantity
  });
});

// Route to reserve a product by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10),
   product = getItemById(itemId);

  if (!product) {
    res.json({'status': 'Product not found'});

return;
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity >= product.initialAvailableQuantity) {
    res.json({'status': 'Not enough stock available',
itemId});

return;
  }

  await reserveStockById(itemId, currentQuantity + 1);
  res.json({'status': 'Reservation confirmed',
itemId});
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
