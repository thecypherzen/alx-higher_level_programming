#!/usr/bin/node
/** prints all characters of a Star Wars movie:
 *  in same order as they are listed in the api
 *  - first argument is the Movie ID - eg: 3 => “Return of the Jedi”
 *  - display one character name per line
 *  - must use the Star wars API
 *  - must use the module '
 */

const request = require('request');

// make request
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err.message);
      } else {
        resolve(res.body);
      }
    });
  });
}

// handle actors
async function getActors (url) {
  const films = await makeRequest(url);
  const actors = films.characters;
  const resList = [];
  let actorData;
  for (const actor of actors) {
    actorData = await makeRequest(actor);
    // console.log(actorData.name);
    resList.push(actorData.name);
  }
  return resList;
}

// Entry point
async function main () {
  const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
  const resList = await getActors(url);
  for (const item of resList) {
    console.log(item);
  }
}
main();
