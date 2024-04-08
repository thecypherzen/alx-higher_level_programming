#!/usr/bin/node

/**
 * A script that searches the second biggest integer in the list of arguments.
 * +The args are passed to script
 * Assumes that all args can be parsed to ints
 * If no arg is passed or number of args passed is 1, 0 is printed
 * Use of 'var's is not allowed
 */

let { argv } = require('node:process');
if (argv.length <= 3) {
  console.log(0);
} else {
  argv = argv.slice(2);
  argv.sort((m, n) => n - m);
  console.log(argv[1]);
}
