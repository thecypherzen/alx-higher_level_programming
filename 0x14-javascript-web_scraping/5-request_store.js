#!/usr/bin/node
/**
 * gets the contents of a webpage and stores it in a file.
 * - the `URL` to request is passed as first argument.
 * - the file path to store the body response is the second argument
 * - uses the `request` module
 */

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(filename, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
