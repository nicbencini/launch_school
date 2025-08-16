let rlSync = require('readline-sync');

function multiply(){
let firstNumber = rlSync.question("Enter the first number: \n");
let secondNumber = rlSync.question("Enter the second number: \n");

return firstNumber * secondNumber
}


console.log(multiply());