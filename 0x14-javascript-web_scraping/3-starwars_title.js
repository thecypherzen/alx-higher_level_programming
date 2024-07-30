#!/usr/bin/node
/**
 * prints the title of a `Star Wars movie` where the episode number
 * + matches a given integer.
 * - the `movie id` is passed as first argument
 * - uses the `star wars api` with the endpoint:
 *   + <https://swapi-api.alx-tools.com/api/films/:id>
 * - uses `request` module
 */

const argv = process.argv;
const request = require('request');

if (argv.length > 2) {
  const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      console.log(JSON.parse(body).title);
    }
  });
}
