#!/usr/bin/node

/**
 * A script that prints a square
 * The size of the square is passed as an argument to the script
 * +If the first argument can’t be converted to an integer, it
 * +prints “Missing size"
 * The square is printed using the character 'X'
 * One loop must be used and use of 'var' is not allowed
 */

const { argv } = require('node:process');
const size = parseInt(argv[2]);
let width, height, square;

square = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (height = size; height; height--) {
    for (width = size; width; width--) {
      square += 'X';
    }
    square += height > 1 ? '\n' : '';
  }
  if (square) { console.log(square); }
}
