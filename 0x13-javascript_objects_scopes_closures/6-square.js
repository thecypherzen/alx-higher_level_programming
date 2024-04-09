#!/usr/bin/node

/**
 * A script that defines a square.
 *  -> It inherits from the Square class of '5-square.js' module
 *  -> creates an instance method called charPrint(c) that prints the
 *     +rectangle using the character 'c' passed to the method
 *  -> If c is undefined, use the character X
 */

const dSquare = require('./5-square');

class Square extends dSquare {
  charPrint (c) {
    const chr = c ?? 'undefined';
    if (chr === 'undefined') {
      this.print();
    } else {
      let i, j, res;
      res = '';
      for (i = this.width; i > 0; i--) {
        for (j = this.width; j > 0; j--) {
          res += chr;
        }
        if (i > 1) { res += '\n'; }
      }
      console.log(res);
    }
  }
}

module.exports = Square;
