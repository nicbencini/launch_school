let rlSync = require('readline-sync');
let firstName = rlSync.question("What's your first name?\n");
let surname = rlSync.question("What is your last name?");
console.log(`Hello, ${firstName} ${surname}!`);