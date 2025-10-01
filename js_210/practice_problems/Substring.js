/*
Problem: Write a function that returns a substring of a string based on a starting index and length.

Algorithm:
- determine starting point of loop 
- cycle through charteres by lenght and add to output stirng

*/

function substr(string, start, length) {
  
  outputString = '';

  if (start < 0){
    start = Number(string.length + start);
  }

  if (start + length > string.length){
    length = string.length - start;
  }


  for (let i = start; i < start + length; i++){
    outputString += string[i];
  }

  console.log(outputString);


}

let string = 'hello world';

substr(string, 2, 4);      // "llo "
substr(string, -3, 2);     // "rl"
substr(string, 8, 20);     // "rld"
substr(string, 0, -20);    // ""
substr(string, 0, 0);      // ""
