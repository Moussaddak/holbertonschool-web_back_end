import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', (error) => {
    console.log('Redis client connected to the server');
});
subscriber.on('error', (error) => {
    console.error('Redis client not connected to the server: ERROR_MESSAGE');
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
    console.log(message);
});

