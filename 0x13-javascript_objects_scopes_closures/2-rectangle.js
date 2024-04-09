#!/usr/bin/node

/**
 * A script that adds functionality to the rectangle class
 *  -> adds constructor that takes in 2 args: 'w' and 'h'
 *  -> initialize the instance attribute width with the value of w
 *  -> initialize the instance attribute height with the value of h
 *  -> If w or h is equal to 0 or not a positive integer, create an empty object
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
