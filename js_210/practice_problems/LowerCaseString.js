/*
Problem:
- Write a function that returns a string converted to lowercase.

Algorithm:
- cycle through each char in the string.
- Get asciinumber for that char
- Check that asciinumber is a capital letter.
- If so convert to lowercase
- Return string


*/

function toLowerCase(string) {

  outputString = ''
  
  for (let i = 0; i < string.length; i ++){
    let asciiNumeric = string.charCodeAt(i);
    if ((asciiNumeric >= 65) && (asciiNumeric <= 90)){
      outputString += String.fromCharCode(asciiNumeric + 32);
    } else {
      outputString += string[i];
    }
  }

  console.log(outputString);

}

toLowerCase('AZ'); 

toLowerCase('ALPHABET');    // "alphabet"
toLowerCase('123');         // "123"
toLowerCase('abcDEF');      // "abcdef"