
function slice(arr, startIdx, endIdx){

  let outputArr = [];

  for (let i = startIdx; i < endIdx; i++){
    push(outputArr, arr[i]);
  }

  return outputArr;
}

function push(list, item){
  list[list.length] = item;
  return list.length
}


console.log(slice([1, 2, 3, 4, 5], 0, 2));                      // [ 1, 2 ]
console.log(slice(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 1, 3));  // [ 'b', 'c' ]