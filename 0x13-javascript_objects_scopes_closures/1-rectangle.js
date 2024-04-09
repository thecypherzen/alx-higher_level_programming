#!/usr/bin/node

/**
 * A script that adds functionality to the rectangle class
 * New Additions:
 *    -> adds constructor that takes in 2 args: 'w' and 'h'
 *    -> initialize the instance attribute width with the value of w
 *    -> initialize the instance attribute height with the value of h
 */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
