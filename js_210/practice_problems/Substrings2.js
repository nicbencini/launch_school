/*

Rules:
- If both start and end are positive integers, start is less than end, and both are within the boundary of the string, return the substring from the start index (inclusive), 
  to the end index (NOT inclusive).
- If the value of start is greater than end, swap the values of the two, then return the substring as described above.
- If start is equal to end, return an empty string.
- If end is omitted, the end variable inside the function isundefined. Return the substring starting at position start up through (and including) the end of the string.
- If either start or end is less than 0 or NaN, treat it as 0.
- If either start or end is greater than the length of the string, treat it as equal to the string length.
*/

function substring(string, start, end) {

  let subString = '';

  if(Number.isNaN(Number(start))|| !typeof(start, Number) || start < 0) {
    start = 0;
  }

  if(end === undefined){
    end = string.length;
  }else if (Number.isNaN(Number(end)) || !typeof(end, Number) || end < 0){
    end = 0;
  }

  if(start > string.lenght){
    start = string.length;
  }

  if(end > string.length){
    end = string.length;
  }

  if (end < start){
    oldStart = start;
    start = end;
    end = oldStart;
  }


  for (let i = start; i < end; i ++){
    subString += string[i];
  }
  
  
  console.log(subString);
  // …
}

let string = 'hello world';

substring(string, 2, 4);    // "ll"
substring(string, 4, 2);    // "ll"
substring(string, 0, -1);   // ""
substring(string, 2);       // "llo world"
substring(string, 'a');     // "hello world"
substring(string, 8, 20);   // "rld"