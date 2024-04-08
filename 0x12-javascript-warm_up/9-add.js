#!/usr/bin/node

/**
 * A function that prints the addition of 2 integers
 * Must use a function of the form: function 'add(a, b)'
 * Use of 'var' not allowed.
 */

function add (a, b) {
  return (a + b);
}

const { argv } = require('node:process');
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

console.log(add(a, b));
