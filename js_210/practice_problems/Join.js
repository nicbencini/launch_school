

function join(arr, str){

  let outputString = '';

  for (let i = 0; i < arr.length; i++){
    outputString += arr[i];

    if (i < arr.length - 1){
      outputString += str;
    }
  }

  return outputString;
}

console.log(join(['bri', 'tru', 'wha'], 'ck '));       // 'brick truck wha'
console.log(join([1, 2, 3], ' and '));                 // '1 and 2 and 3'