

function concat(arr1, arr2){

  outputArr = [];

  for (let i = 0; i < arr1.length; i++){
    push(outputArr, arr1[i]);   
  }

  for (let i = 0; i < arr2.length; i++){
    push(outputArr, arr2[i]);
  }

  return outputArr;
}

function push(list, item){
  list[list.length] = item;
  return list.length
}

console.log(concat([1, 2, 3], [4, 5, 6]));       // [ 1, 2, 3, 4, 5, 6 ])