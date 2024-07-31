#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * - the `MOVIE ID` is passed as first argument:
 * - displays one character name per line
 * - uses the `STAR WARS` api
 * - uses the `request` module
 */

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const request = require('request');

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body.characters.map(actor => {
      request(actor, { json: true }, (err, res, body) => {
        if (err) {
          console.log(err);
          return null;
        }
        console.log(body.name);
      });
      return null;
    });
  }
});
