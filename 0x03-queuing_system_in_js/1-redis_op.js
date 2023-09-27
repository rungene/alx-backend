import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    if (error) {
      redis.print('Error:', error);
    } else {
      redis.print(`Reply: ${reply}`);
    }
    client.quit();
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, value) => {
    if (error) {
      console.error('Error:', error);
    } else {
      redis.print(value);
    }
    client.quit();
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
