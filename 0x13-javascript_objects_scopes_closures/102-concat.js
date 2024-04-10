#!/usr/bin/node

/**
 * A script that reads two files, concatenates them and writes the
 * +result to another file
 */
const fs = require('fs');
const { argv } = require('node:process');
argv.splice(0, 2);
const [fileA, fileB, dest] = argv;

// i/o operations
const res = fs.readFileSync(fileA) + fs.readFileSync(fileB);
fs.writeFileSync(dest, res);
