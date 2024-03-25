#!/usr/bin/node
// this Script Print the factorial of a number
function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
