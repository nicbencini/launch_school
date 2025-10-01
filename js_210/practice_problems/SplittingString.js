function splitString(inputString, delimiter){

  found = false;

  outputList = [];

  let word = '';

  if((delimiter === undefined) || (delimiter === '')){
    for (let i = 0; i < inputString.length; i++){
        word += char;
        outputList.push(word);
        word = '';
      }
  } else {
    for (let i = 0; i < inputString.length; i++){
      
      char = inputString[i];

      if (char !== delimiter){
        word += char;
      } else{
        outputList.push(word);
        word = '';
      }
    }
    if (word !== ''){
      outputList.push(word);
    }
    
  }
  console.log(outputList);

}

splitString('abc,123,hello world', ',');
// logs:
// abc
// 123
// hello world

splitString('hello');
// logs:
// ERROR: No delimiter

splitString('hello', '');
// logs:
// h
// e
// l
// l
// o

splitString('hello', ';');
// logs:
// hello

splitString(';hello;', ';');
// logs:
//  (this is a blank line)
// hello