#!/usr/bin/node
/** displays the status of a get request
 *  - the first arg is the url to the resource
 *  - the status code must be printed like this: code: <status code>
 *  - must use the module request
 */

const request = require('request');
const { argv } = require('node:process');
const url = `${argv[2]}`;

request(url, (err, res, body) => {
  if (!err) {
    console.log('code:', res.statusCode);
  }
});
