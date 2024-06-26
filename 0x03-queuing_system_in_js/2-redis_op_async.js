/* eslint-disable one-var */
/* eslint-disable require-jsdoc */
/* eslint-disable func-style */
import {promisify} from 'util';
import redis from 'redis';

const client = redis.createClient();
// Promisify the client.get method
const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);

    console.log(value);
  } catch (err) {
    console.error('Error fetching value:', err);
  }
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

function setNewSchool (schoolName, value) {
    client.set(schoolName, value, redis.print);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
