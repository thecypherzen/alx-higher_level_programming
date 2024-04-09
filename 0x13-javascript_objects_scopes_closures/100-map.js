#!/usr/bin/node

/**
 *  A script that imports an array and computes another
 *  Imports 'list' from '100-data.js'
 *  Map function must be used
 *  The new list is created by multiplying the element in list by its
 *  +corresponding index.
 *  Prints both lists when done.
 */

const list = require('./100-data').list;
const newArray = list.map((val, idx) => idx * val);
console.log(list);
console.log(newArray);
