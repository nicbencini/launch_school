function checkGoldbach(number){

  let output = '';


  for (let i = number; i >= 1; i--){
    let number1 = i;
    let number2 = number - i;

    if (((isPrime(number1) && isPrime(number2)) &&
        (number1 <= number2))){
      output += '\n' + number1 + ' ' + number2
    }
  }

  console.log('logs:' + output);
}

function isPrime(number){

  if (number <2 ){
    return false;
  }

  for (let i = 2; i < number; i++){
    if (number % i === 0){
      return false;
    }
  }

  return true;
}

checkGoldbach(3);
// logs: null

checkGoldbach(4);
// logs: 2 2

checkGoldbach(12);
// logs: 5 7

checkGoldbach(100);
// logs:
// 3 97
// 11 89
// 17 83
// 29 71
// 41 59
// 47 53