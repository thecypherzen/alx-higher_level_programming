#!/usr/bin/node
/** computes the number of tasks completed by user id
 *  - the first argument is the API URL:
 *     https://jsonplaceholder.typicode.com/todos
 *  - only prints users with completed task
 *  - must use the module 'request'
 */

const request = require('request');
const url = process.argv[2];
const taskMap = {};
request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.log(err.message);
  } else {
    if (res.statusCode === 200) {
      res.body.forEach((task) => {
        if (task.completed) {
          taskMap[task.userId] = (taskMap[task.userId] || 0) + 1;
        }
      });
      console.log(taskMap);
    } else {
      console.log('code:', res.statusCode);
    }
  }
});
