exports.handler = async (event) => {
    // Extract the 'name' and 'video_id' from the event
    const name = event.name;
    const video_id = event.video_id;

    // Create a response object that includes the extracted parameters
    const response = {
        statusCode: 200,
        body: JSON.stringify({
            message: 'Hello from Lambda!',
            name: name,
            video_id: video_id
        }),
    };

    return response;
};

const fs = require('fs');

// Function to load credentials from creds.json
function loadCredentials(name) {
    // Read the creds.json file
    const rawData = fs.readFileSync('rav_creds.json');
    const creds = JSON.parse(rawData);

    // Loop through each item in the creds array
    for (const item of creds) {
        if (item[name]) {
            return item[name];
        }
    }
    return null;
}

// Example usage
// const nameToLoad = 'classic'; // Change this to 'mergui' to load different credentials
// const credentials = loadCredentials(nameToLoad);

// if (credentials) {
//     console.log(`Email: ${credentials.email}`);
//     console.log(`Password: ${credentials.pass}`);
// } else {
//     console.log(`No credentials found for name: ${nameToLoad}`);
// }



function writeEnvFile(credentials) {
    const envData = `SPOTIFY_EMAIL=${credentials.email}\nSPOTIFY_PASSWORD=${credentials.pass}\nPUPETEER_HEADLESS=true\n`;
    fs.writeFileSync('.env-test', envData);
}

function writeEpisodeFile(id) {
    const episodeData = { id: id };
    fs.writeFileSync('episode.json', JSON.stringify(episodeData, null, 2));
}


// Example usage
const nameToLoad = 'classic'; // Change this to 'mergui' to load different credentials
const credentials = loadCredentials(nameToLoad);

if (credentials) {
    console.log(`Email: ${credentials.email}`);
    console.log(`Password: ${credentials.pass}`);
    writeEnvFile(credentials);
    console.log('.env file has been created with the credentials.');
    writeEpisodeFile('abc')
} else {
    console.log(`No credentials found for name: ${nameToLoad}`);
}
