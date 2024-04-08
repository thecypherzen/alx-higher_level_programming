#!/usr/bin/node

/**
 * A script that defines a function and exports it
 * The function sums two numbers
 */

function add (a, b) {
  return (a + b);
}

module.exports.add = add;
