import redis from 'redis';

const client = redis.createClient();
const myChannel = 'holberton school channel';

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
  client.subscribe(myChannel);
});

client.on('message', (channel, message) => {
  console.log(`Received message from ${channel}: ${message}`);

  if (message === 'KILL_SERVER') {
    console.log('Recieved "KILL_SERVER" message, Unsubscribing');
    client.unsubscribe(myChannel);
    client.quit();
  }
});
