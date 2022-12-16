#!/usr/bin/node
// const url = process.argv[2];
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) console.log(err);
  let list = [];
  for (const film of JSON.parse(body).results) { // access `results` key
    list = list.concat(film.characters); // save all `characters` list in one list
  }
  // console.log(list);
  const uniq = list.filter(x => x.includes('18')); // create a new array, just with `18` id
  console.log(uniq.length);
});
