#!/usr/bin/node
// this Script Print the sum of tow number
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
console.log(add(process.argv[2], process.argv[3]));
