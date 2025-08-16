let arr = ['a', 'abcd', 'abcde', 'abc', 'ab'];

function oddLengths (inputArray){
  
  return inputArray.reduce((acc, ele) => {
          if(ele.length % 2 === 1){
            return acc.push(ele.length);
          }},[]);
 
  }


console.log(oddLengths(arr)); // => [1, 5, 3]