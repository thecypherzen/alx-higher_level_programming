#!/usr/bin/node
/**
 * computes the number of tasks completed by user id.
 * - the `URL` to request is passed as first argument:
 *   <https://jsonplaceholder.typicode.com/todos>
 * - only users with completed tasks are printed
 * - uses the `request` module
 */

const url = process.argv[2];
const request = require('request');

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const result = {};
    body.map(todo => {
      if (todo.completed) {
        result[todo.userId] = (result[todo.userId] ?? 0) + 1;
      }
      return null;
    });
    console.log(result);
  }
});
