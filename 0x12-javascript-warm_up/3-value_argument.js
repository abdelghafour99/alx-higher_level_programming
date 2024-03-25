#!/usr/bin/node
// this Script Print the first argument passed throw it
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
