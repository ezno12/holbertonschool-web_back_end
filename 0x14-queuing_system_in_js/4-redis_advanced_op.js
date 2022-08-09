import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

client.on('connect', () => { console.log('Redis client connected to the server'); });


client.hSet('HolbertonSchools', ...Object.entries({
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}), print)

client.hGetAll('HolbertonSchools', (err, replay) => {
    console.log(replay)
})