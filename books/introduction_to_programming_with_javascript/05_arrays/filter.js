let numbers1 = [1, 3, 5, 7, 9, 11];
let numbers2 = [];
let numbers3 = [2, 4, 6, 8];

function checkFor3 (inputArray){
  
  let checkList = inputArray.filter(x => x === 3);

  return checkList.length > 0;

}

console.log(checkFor3(numbers1));
console.log(checkFor3(numbers2));
console.log(checkFor3(numbers3));