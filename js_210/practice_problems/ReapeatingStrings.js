/*

Problem:
Implement a function that takes a string and a number times as arguments. 
The function should return the string repeated times number of times. If times is not a number, return undefined. If it is a negative number, return undefined also. 
If times is 0, return an empty string. You may ignore the possibility that times is a number that isn't an integer.

Rules:
- Function repeats string number of times.
- If times is not a number return undefined.
- If it is a negative number also return undefined.
- If times is 0 return an empty string.
- Ignore possibility that times may not be an integer.
- You may concatenate strings, but you may not use any other properties or methods from JavaScript's built-in String class.

Algorithm:
- Check that times is an acceptable type.
- If it is :
    - Create for loop for number of times
    - Add string to the end of an output string using for loop
    - Return output string.

*/

function repeat(string, times) {
  
  let outputString = '';

  if ((!typeof(times, Number))||(Number < 0)){
    outputString = undefined;
  } else {

    for (let i = 0; i < times; i ++){
      outputString += string;
    }
  }

  console.log('\"' + outputString + '\"');

}

repeat('abc', 1);       // "abc"
repeat('abc', 2);       // "abcabc"
repeat('abc', -1);      // undefined
repeat('abc', 0);       // ""
repeat('abc', 'a');     // undefined
repeat('abc', false);   // undefined
repeat('abc', null);    // undefined
repeat('abc', '  ');    // undefined