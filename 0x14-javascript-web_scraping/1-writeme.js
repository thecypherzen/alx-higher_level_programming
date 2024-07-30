#!/usr/bin/node
/**
 * writes a string to a file
 * - the `filename` is passed as first argument
 * - the `string` is passed as second argument
 * - content of the file must be written in utf-8
 * - if an error occurrs, the error object is printed
 */

const fs = require('fs');
const argv = process.argv;

if (process.argv.length > 3) {
  fs.writeFile(argv[2], argv[3], (err) => {
    if (err) {
      console.log(err);
    }
  });
}
