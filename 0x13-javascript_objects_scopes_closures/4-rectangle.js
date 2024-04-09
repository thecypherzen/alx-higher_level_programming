#!/usr/bin/node

/**
 * A script that adds functionality to the rectangle class
 *  -> adds constructor that takes in 2 args: 'w' and 'h'
 *  -> initialize the instance attribute width with the value of w
 *  -> initialize the instance attribute height with the value of h
 *  -> If w or h is equal to 0 or not a positive integer, create an empty object
 *  -> Creates an instance method called print() that prints the rectangle
 *     +using the character X
 *  -> Creates an instance method called 'rotate()' that exchanges the width
 *     +and the height of the rectangle
 *  -> Creates an instance method called 'double()' that multiples the width
 *     +and the height of the rectangle by 2
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method that rotates dimentions
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // method that doubles rectangle dimensions
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  // method that prints the rectangle
  print () {
    let i, j, res;
    res = '';
    for (i = this.height; i > 0; i--) {
      for (j = this.width; j > 0; j--) {
        res += 'X';
      }
      if (i > 1) { res += '\n'; }
    }
    console.log(res);
  }
}

module.exports = Rectangle;
