#!/usr/bin/node

/* A script that prints the first argument passed to it
   If no arguments are passed to the script, it prints “No argument”
   Use of length is not allowed
*/

const { argv } = require('node:process');
const firstArg = argv?.[2];
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
