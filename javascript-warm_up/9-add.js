#!/usr/bin/node
function add (a, b) {
  return a + b;
}
// Number() method returns NaN if the argument cannot be converted to a number
console.log(add(Number(process.argv[2]), Number(process.argv[3])));
