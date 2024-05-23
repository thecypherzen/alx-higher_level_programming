#!/usr/bin/node
/** prints the number of movies where the character “Wedge Antilles”
 *  is present.
 *  - The first argument is the API URL of the Star wars API:
 *     'https://swapi-api.alx-tools.com/api/films'
 *  - Wedge Antilles is character ID 18 - your script must use this ID
 *     for filtering the result of the API
 *  - must use the module request
 */

const request = require('request');
const url = `${process.argv[2]}`;

request(url, { json: true }, (err, res, body) => {
  // console.log(url);
  if (err) {
    console.log(err);
  } else {
    if (res.statusCode === 200) {
      const regex = /[*]*18/;
      const results = body?.results;
      let temp;
      /* solution using for...of => watch {varnames}
      let count = 0;
      // console.log(results);
      for (const result of results) {
        for (const actor of result.characters) {
          if (regex.test(actor)) {
            count += 1;
          }
        }
      }
      console.log(count);
      */
      // solution using reduce
      const count = results.reduce((acc, film) => {
        temp = film.characters.reduce((ac, actor) => {
          if (regex.test(actor)) {
            return ac + 1;
          } else {
            return ac;
          }
        }, 0);
        return temp + acc;
      }, 0);
      console.log(count);
    }
  }
});
