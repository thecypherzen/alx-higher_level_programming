#!/usr/bin/node
/** prints the title of a Star Wars movie where the episode number matches a
 *  given integer.
 *  - The first argument is the movie ID
 *  - must use the Star wars API with the endpoint:
 *    https://swapi-api.alx-tools.com/api/films/:id
 *  - must use the module request
 */

const request = require('request');
const { argv } = require('node:process');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, { json: true }, (err, res, body) => {
  if (!err) {
    console.log(res?.body?.title);
  }
});
