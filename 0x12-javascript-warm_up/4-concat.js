#!/usr/bin/node
/*
  A script that prints two arguments passed to it, in the following
  + format: “ is ”
  + Example: argA is argB
  Use of 'var' not allowed
*/

const { argv } = require('node:process');
const myStr = argv[2] + ' is ' + argv[3];
console.log(myStr);
