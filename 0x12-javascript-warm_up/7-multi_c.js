#!/usr/bin/node

/**
 * A script that prints 'C is fun' n times.
 * where n is passed as argument.
 * If n cannot be parsed to an integer, it prints
 * 'Missing number of occurrences'
 */

const { argv } = require('node:process');
let nTimes;

nTimes = parseInt(argv[2]);
if (isNaN(nTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (; nTimes > 0; nTimes--) {
    console.log('C is fun');
  }
}
