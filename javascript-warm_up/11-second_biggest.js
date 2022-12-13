#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv.length === 3) {
  console.log('0');
} else {
  // `sort((a, b) => b - a)` is the same as `sort(function(a ,b){return b -a})`
  const secBiggest = process.argv.slice(2).sort((a, b) => b - a)[1];
  console.log(secBiggest);
}
