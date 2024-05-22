#!/usr/bin/node
/** prints all characters of a Star Wars movie:
 *  - first argument is the Movie ID - eg: 3 => “Return of the Jedi”
 *  - display one character name per line
 *  - must use the Star wars API
 *  - must use the module '
 */

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err.message);
  } else {
    if (res.statusCode === 200) {
      // console.log(body);
      const actors = body.characters;
      actors.forEach((actor) => {
        request(actor, { json: true }, (err, res, body) => {
          if (err) {
            console.log(err.message);
          }
          console.log(body.name);
          return body.name;
        });
      });
    } else {
      console.log(res.statusCode);
    }
  }
});
