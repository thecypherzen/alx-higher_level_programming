#!/usr/bin/node

/**
 *  A script that imports a dictionary of occurrences by user id and computes
 *  +a dictionary of user ids by occurrence.
 *  -> import dict from the file 101-data.js
 *  -> In the new dictionary:
 *     -> A key is a number of occurrences
 *     -> A value is the list of user ids
 *  -> prints the new dictionary at the end
 */
const dict = require('./101-data').dict;
const newDict = {};
for (const [key, val] of Object.entries(dict)) {
  if (newDict[val] === undefined) {
    newDict[val] = [key];
  } else {
    newDict[val].push(key);
  }
}
console.log(newDict);
