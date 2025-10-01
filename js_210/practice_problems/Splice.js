
function splice(arr, startIdx, number){

  let outputArr = [];

  let endIdx = startIdx + number;

  let firstSection = slice(arr,0, startIdx);
  let secondSection = slice(arr, startIdx, endIdx);
  let thirdSection = slice(arr, endIdx, arr.length );

  arr.length = startIdx;
  for (let i = 0; i < thirdSection.length; i++){
    push(arr, thirdSection[i]);
  }

  return secondSection;
}

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

let count = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(splice(count, 2, 5));                   // [ 3, 4, 5, 6, 7 ]
console.log(count);                                 // [ 1, 2, 8 ]
