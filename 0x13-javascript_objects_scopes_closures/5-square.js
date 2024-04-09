#!/usr/bin/node

/**
 * A script that defines a square.
 *  -> It inherits from the Rectangle class of '4-rectangle.js' module
 *  -> Constructor takes in 1 argument 'size'
 *  -> Rectangle class must be called using 'super()'
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
