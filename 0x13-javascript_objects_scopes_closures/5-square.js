#!/usr/bin/node
// A class Rectangle that defines a rectangle
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
