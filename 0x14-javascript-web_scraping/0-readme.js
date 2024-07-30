#!/usr/bin/node
/**
 * reads and prints content of a file to stdout
 * - the file is passed as an argument
 * - content of the file must be read in utf-8
 * - if an error occurrs, the error object is printed
 */

const fs = require('fs');

if (process.argv.length > 2) {
  fs.readFile(process.argv[2], 'utf-8', (err, data) => {
    if (!err) { console.log(data); } else { console.log(err); }
  });
}
