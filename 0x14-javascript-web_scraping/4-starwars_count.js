#!/usr/bin/node
/** prints the title number of movies where the character “Wedge Antilles”
 *  is present.
 *  - The first argument is the API URL of the Star wars API:
 *     'https://swapi-api.alx-tools.com/api/films/'
 *  - Wedge Antilles is character ID 18 - your script must use this ID
 *     for filtering the result of the API
 *  - must use the module request
 */

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, (err, res, body) => {
  // console.log(url);
  if (err) {
    console.log(err);
  } else {
    if (res.statusCode === 200) {
      const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
      let results = res?.body?.results;
      results = results.filter(
        (film) => film.characters.includes(wedgeUrl)
      );
      console.log(results.length);
    }
  }
});
