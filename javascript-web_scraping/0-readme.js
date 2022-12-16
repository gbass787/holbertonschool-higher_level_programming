#!/usr/bin/node
const fs = require('fs');
/*
first argument: path or file you want to be read
second argument: optional object in this case encoding utf-8
third argument: callback function executed when the file is read,
  this callback function has two arguments: an error object and the
  data from the file
*/
fs.readFile(process.argv[2], 'utf-8', (error, content) => {
  console.log(error || content);
});
