import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Error ${error}`);
});

const hashKey = 'HolbertonSchools';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.hset(hashKey, 'Portland', '50', redis.print);
client.hset(hashKey, 'Seattle', '80', redis.print);
client.hset(hashKey, 'New York', '20', redis.print);
client.hset(hashKey, 'Bogota', '20', redis.print);
client.hset(hashKey, 'Cali', '40', redis.print);
client.hset(hashKey, 'Paris', '2', redis.print);

client.hgetall(hashKey, (error, hashData) => {
  if (error) {
    console.error(`Error ${error}`);
  } else {
    console.log(hashData);
  }
  client.quit();
});
