const PASSWORD = 'password';

check_count = 0;

while (true){
  let guess = prompt("What is the password:");

  if (guess === PASSWORD){
    console.log('You have successfully logged in.');
  }

  check_count += 1;
  
  if (check_count === 3) {
    console.log('You have been denied access.');
    break;
  }
  
}