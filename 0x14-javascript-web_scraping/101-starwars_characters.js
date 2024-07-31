#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie in same order as api
 * - the `MOVIE ID` is passed as first argument:
 * - displays one character name per line
 * - uses the `STAR WARS` api
 * - uses the `request` module
 */

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const request = require('request');

request(url, { json: true }, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    (async (characters) => {
      for (const url of characters) {
        const actorName = await (actorUrl => {
          return new Promise((resolve, reject) => {
            request(actorUrl, { json: true }, (err, res, body) => {
              if (!err && res.statusCode === 200) {
                resolve(res.body.name);
              } else {
                reject(err);
              }
            });
          });
        })(url);
        console.log(actorName);
      }
    })(body.characters);
  }
});
