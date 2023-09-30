import redis from 'redis';
import util from 'util';

const client = redis.createClient();
const express = require('express');
const app = express();
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

const getAsync = util.promisify(client.get).bind(client);
const setAsync = util.promisify(client.set).bind(client);

function getItemById(id) {
  return listProducts.find((listData) => listData.id === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item:${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item:${itemId}`);
  return stock ? parseInt(stock) : 0;
}
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
