
function trim (inputWord){

  let outputWord = '';

  for (let i = 0; i < inputWord.length; i++){
    let char = inputWord[i];

    if (char !== ' '){
      outputWord = inputWord.slice(i);
      break;
    }

  }

  for (let j = outputWord.length -1; j >= 0; j--){
    let char = outputWord[j];

    if (char !== ' '){
      outputWord = outputWord.slice(0,j+1);
      break;
    }
  }

  console.log("\'" + outputWord + "\'");

}

trim('  abc  ');  // "abc"
trim('abc   ');   // "abc"
trim(' ab c');    // "ab c"
trim(' a b  c');  // "a b  c"
trim('      ');   // ""
trim('');     