#!/usr/bin/node
// Writes a string to a file

const { argv } = require('node:process');
const fs = require('node:fs');

if (argv.length < 3) {
  process.exit();
}

const file = argv[2];
const content = argv[3];

fs.writeFile(file, content, (error) => {
  if (error) {
    console.log(error);
  }
});
