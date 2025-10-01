/*
Write two functions that each take two strings as arguments. Their expected behaviors are as follows:

The indexOf function searches for the first instance of a substring in firstString that matches the string secondString, and returns the index of the character where that substring begins.

The lastIndexOf function searches for the last instance of a substring in firstString that matches the string secondString, and returns the index of the character where that substring begins.

Both functions return -1 if firstString does not contain the substring specified by secondString.

Algorithm:
indexOf:
- Cycle through string
- Check if character matches subString. if yes:
  - Cycle through each character in substring
  - If all characters are a match return True
- If so return index
- If no match found return -1;

lastIndexOf:
- cycle through string in reverse order
- same process as above

Examples:

'Blue Whale', 'Whale'



*/


function indexOf(inputString, subString){

  for (let i = 0; i < inputString.length; i++){
    let match = true;

    for (let j = 0; j < subString.length; j++){
      if (inputString[i + j] !== subString[j]){
        match = false;
      }
    }

    if (match === true){
      return i;
    }
  }
  return -1;
}

function lastIndexOf(inputString, subString){

  for (let i = inputString.length; i >= 0; i--){
    let match = true;

    for (let j = subString.length; j >= 0; j--){
      if (inputString[i + j] !== subString[j]){
        match = false;
      }
    }

    if (match === true){
      return i;
    }
  }

  return -1;


}




console.log(indexOf('Some strings', 's'));                      // 5
console.log(indexOf('Blue Whale', 'Whale'));                    // 5
console.log(indexOf('Blue Whale', 'Blute'));                    // -1
console.log(indexOf('Blue Whale', 'leB'));                      // -1

console.log(lastIndexOf('Some strings', 's'));                  // 11
console.log(lastIndexOf('Blue Whale, Killer Whale', 'Whale'));  // 19
console.log(lastIndexOf('Blue Whale, Killer Whale', 'all'));    // -1
