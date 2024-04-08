#!/usr/bin/node

/**
 * A script that computes and prints a factorial
 *    It must be done recursively
 * The value to calculated is passed as an arg to the script
 * Note: Factorial of NaN is 1
 */

const { argv } = require('node:process');
const vNum = parseInt(argv[2]);

function fact (num) {
  if (!num) { return (1); }
  return num * fact(num - 1);
}

console.log(fact(vNum));
