#!/usr/bin/node
/*  prints  statements  based  on  arguments  passed  to  script  */

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
