import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
  console.error(`Error ${error}`);
});

const hashKey = 'HolbertonSchools';

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.hset(
  hashKey,
  'Portland',
  '50',
  'Seattle',
  '80',
  'New York',
  '20',
  'Bogota',
  '20',
  'Cali',
  '40',
  'Paris',
  '2',
  (error, reply) => {
    if (error) {
      console.error(`Error ${error}`);
    } else {
      console.log('Reply:', reply);
    }

    client.hgetall(hashKey, (error, hashData) => {
      if (error) {
        console.error(`Error ${error}`);
      } else {
        console.log(hashData);
      }
      client.quit();
    });
  }
);
