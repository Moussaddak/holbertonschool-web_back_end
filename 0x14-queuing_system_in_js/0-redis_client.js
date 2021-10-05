import redis from 'redis';

const client = redis.createClient();
client.on('connect', (error) => {
    console.log('Redis client connected to the server');
});
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});
