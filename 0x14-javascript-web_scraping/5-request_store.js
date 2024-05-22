#!/usr/bin/node
/** gets the contents of a webpage and stores it in a file.
 *  - the first argument is the URL to request
 *  - the second argument the file path to store the body response
 *  - the file must be UTF-8 encoded
 *  - must use the module 'request'
 */

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    if (res.statusCode === 200) {
      fs.writeFile(path, body, (error) => {
        if (error) {
          console.log(error);
        }
      });
    }
  }
});
