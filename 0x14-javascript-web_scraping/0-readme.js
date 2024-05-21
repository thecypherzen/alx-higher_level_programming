#!/usr/bin/node
// Reads a file and prints its content to stdout

const { argv } = require('node:process');
const fs = require('node:fs');
const file = argv[2];
const encoding = 'utf-8';

fs.readFile(file, encoding, (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
