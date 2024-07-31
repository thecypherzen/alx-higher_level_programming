#!/usr/bin/node
/**
 * gets the contents of a webpage and stores it in a file.
 * - the `URL` to request is passed as first argument.
 * - the file path to store the body response is the second argument
 * - uses the `request` module
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length > 2) {
  const url = `${process.argv[2]}`;
  const filename = `${process.argv[3]}`;

  request(url, { json: true }, (err, response, body) => {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      fs.writeFile(filename, `${body}`, 'utf8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
