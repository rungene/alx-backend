import redis from 'redis';
import util from 'util';

const client = redis.createClient();
const express = require('express');
const app = express();
const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);

function getItemById(id) {
  return listProducts.find((listData) => listData.itemId === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item:${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item:${itemId}`);
  return stock ? parseInt(stock) : 0;
}

app.use((req, res, next) => {
  res.setHeader('Content-Type', 'application/json');
  next();
});

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const currentProduct = getItemById(itemId);
  if(!currentProduct) {
    res.status(404).json({"status":"Product not found"}); 
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({...currentProduct, currentQuantity});
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.status(404).json({"status":"Product not found"});  
  } else {
    const currentQuantity = product.initialAvailableQuantity;
    if (currentQuantity <= 0) {
      res.json({"status":"Not enough stock available","itemId":itemId});  
    } else {
      await reserveStockById(itemId, 1);
      res.json({"status":"Reservation confirmed","itemId":itemId});
    }
  }
});
app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
