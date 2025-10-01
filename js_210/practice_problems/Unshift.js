
function unshift(arr, item){

  for (let i = 0; i < arr.length ; i++){
      
    arr[i + 1] = arr[i];
  }

  arr[0] = item;

  return arr.length;
}

let count = [1, 2, 3];
console.log(unshift(count, 0));      // 4
console.log(count);                  // [ 0, 1, 2, 3 ]