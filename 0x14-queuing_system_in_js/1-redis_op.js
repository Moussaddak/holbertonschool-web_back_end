import redis from 'redis';

const client = redis.createClient();
client.on('connect', (error) => {
    console.log('Redis client connected to the server');
});
client.on('error', (error) => {
    console.error('Redis client not connected to the server: ERROR_MESSAGE');
});

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print);
const displaySchoolValue = (schoolName) => client.get(schoolName,
    (err, reply) => redis.print(reply)
);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
