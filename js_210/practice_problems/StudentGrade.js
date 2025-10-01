

let score1 = prompt('Enter score 1: ');
let score2 = prompt('Enter score 2: ');
let score3 = prompt('Enter score 3: ');

let averageScore = (Number(score1) + Number(score2) + Number(score3))/3;
let scoreString = 'Based on the average of 3 scores your letter grade is '


if (averageScore >= 90){
  console.log(scoreString + '\"A\"');
} else if (averageScore >= 70){
  console.log(scoreString + '\"B\"');
} else if (averageScore >= 50){
  console.log(scoreString + '\"C\"');
} else {
  console.log(scoreString + '\"F\"');
}