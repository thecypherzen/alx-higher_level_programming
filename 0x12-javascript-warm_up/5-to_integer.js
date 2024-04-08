#!/usr/bin/node

/**
   - A script that prints:
   'My number: <first argument converted in integer>'
   if the first argument can be converted to an integer
   - If the argument can’t be converted to an integer, it prints 'Not a number'
   - Use of 'var' and 'try/catch' prohibited
*/

const { argv } = require('node:process');
const myNum = parseInt(argv[2]);

if (!myNum) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
