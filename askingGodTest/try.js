const fs = require('fs');
const path = require('path');

// Load the JSON file
const filePath = path.join('E:', 'Daniel_git', 'askingGodTest', 'stickPoetry.json');
const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));

// Get a random key from the JSON data
// const randomIndex = Math.floor(Math.random() * data.length);
const randomData = data[randomIndex];

// Print the corresponding value 
const values_1 = randomData['stick_poetry'];
console.log(values_1);
const values_2 = randomData['stick_9'];
console.log(values_2);