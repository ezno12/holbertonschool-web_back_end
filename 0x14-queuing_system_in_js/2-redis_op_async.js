import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

client.on('connect', () => { console.log('Redis client connected to the server'); });



function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print)
    
}

async function displaySchoolValue(schoolName) {
    const getKey = client.get(schoolName, (replay) => {
        return replay
    })
    await getKey.then(value => {
        console.log(value)
    })
    
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');