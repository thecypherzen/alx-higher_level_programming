#!/usr/bin/node
/**
 * prints the number of movies where the character `Wedge Antilles`
 * + is present
 * - the `SWAPI URL` is passed as first argument. url passed is:
 *   + <https://swapi-api.alx-tools.com/api/films>
 * - Wedge Antilles is character ID `18` and it's used
 *   + for filtering the results
 * - uses the `request` module
 */

const argv = process.argv;
const request = require('request');

if (argv.length > 2) {
  let total;
  request(`${argv[2]}`, (err, response, body) => {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
      total = films.reduce((eCount, film) => {
        const iCount = film.characters.reduce((acc, actor) => {
          return actor === charUrl ? acc + 1 : acc;
        }, 0);
        return eCount + iCount;
      }, 0);
      console.log(total);
    }
  });
}
