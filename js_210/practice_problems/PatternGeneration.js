function generatePattern(number){

  
  for (let i=1; i < number+1; i++){
    let outputString = '';

    for (let j=1; j < number+1; j++){
      if (j <= i){
        outputString += String(j);
      } else {
        outputString += '*'
      }

    }

    console.log(outputString);
  }
}

generatePattern(9);