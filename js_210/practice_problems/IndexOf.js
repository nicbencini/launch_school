
function indexOf(arr, item){

  let idx = -1;

  for (let i = 0; i < arr.length; i++){
    if (arr[i] === item){
      idx = i;
      break;
    }
  }

  return idx;
}

console.log(indexOf([1, 2, 3, 3], 3));         // 2
console.log(indexOf([1, 2, 3], 4));            // -1