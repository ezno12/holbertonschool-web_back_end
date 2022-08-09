const redis = require('redis');
const subscriber = redis.createClient();

subscriber.on('ready', () => {
    console.log('Redis client connected to the server')
})

subscriberon('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

const channel = 'holberton school channel'

subscriber.subscribe(channel);

subscriber.on('message', (channel, message) => {
  console.log(`${message}`);
  if(message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel)
    process.exit(0)
  }
});
