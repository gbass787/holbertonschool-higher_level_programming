#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
/*
we can also export this module like this:
module.exports = Rectangle;
*/
