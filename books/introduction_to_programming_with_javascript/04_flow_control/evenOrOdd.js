function evenOrOdd(inputNumber){
  
  if (Number.isInteger(inputNumber)){
    if (inputNumber % 2 == 0) {
      console.log('even');
    }
    else {
      console.log('odd');
    }
  } else {
    console.log('Error');
    return;
  }
}

evenOrOdd(7);
evenOrOdd(2);
evenOrOdd('as2');