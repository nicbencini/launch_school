
function pop(array){

  if (array.length === 0){
    return undefined;
  }
  
  let output = array[array.length -1];

  array.length = array.length - 1;

  return output;
}

let count = [1, 2, 3];
console.log(pop(count));             // 3
console.log(count);                  // [ 1, 2 ]