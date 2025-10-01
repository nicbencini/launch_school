
function push(list, item){
  list[list.length] = item;
  return list.length
}

let count = [0, 1, 2];
console.log(push(count, 3));         // 4
console.log(count);   