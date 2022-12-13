#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // filter return an array of the same element, use arrow function syntax
  return list.filter(element => element === searchElement).length;
};
