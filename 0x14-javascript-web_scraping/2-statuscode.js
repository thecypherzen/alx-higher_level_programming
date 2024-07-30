#!/usr/bin/node
/**
 * displays the status code of a `GET` request.
 * - the `url` is passed as first argument
 * - the status code is printed in the format
 *   `code: <status code>`
 * - if an error occurrs, the error object is printed
 * - uses `request` module
 */

const argv = process.argv;
const request = require('request');

if (argv.length > 2) {
  request(argv[2], (err, response) => {
    if (err) {
      console.log(err);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
