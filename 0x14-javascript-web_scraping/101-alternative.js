#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie in same order as api
 * - the `MOVIE ID` is passed as first argument:
 * - displays one character name per line
 * - uses the `STAR WARS` api
 * - uses the `request` module
 * - this implementation uses the `Array.prototype.map()` function.
 */

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const request = require('request');

request(url, { json: true }, async (err, res, body) => {
  if (!err && res.statusCode === 200) {
    const actorNames = await Promise.all(body.characters.map(
      (actorUrl) => {
        return new Promise((resolve, reject) => {
          request(actorUrl, { json: true }, (err, res, actorInfo) => {
            if (!err && res.statusCode === 200) {
              resolve(actorInfo.name);
            } else {
              reject(err);
            }
          });
        });
      }));
      actorNames.map(name => {
	  console.log(name);
      });
  }
});
