/*

Problem:
Implement a function that determines whether a string begins with another string. If it does, the function should return true, or false otherwise.

Rules:
- You may use the square brackets ([]) to access a character by index (as shown below), and the length property to find the string length. However, you may not use any other properties or methods from JavaScript's built-in String class.

Algorithm:
- cyclethrough characters in searchString:
- if character = equivalent character in string continue:
- if not return false

*/

function startsWith(string, searchString) {
  
  for (let i=0; i < searchString.length; i ++){
    if (searchString[i] !== string[i]){
      return false;
    }
  }

  return true;
}

let str = 'We put comprehension and mastery above all else';
console.log(startsWith(str, 'We'));              // true
console.log(startsWith(str, 'We put'));          // true
console.log(startsWith(str, ''));                // true
console.log(startsWith(str, 'put'));             // false

let longerString = 'We put comprehension and mastery above all else!';
console.log(startsWith(str, longerString));      // false