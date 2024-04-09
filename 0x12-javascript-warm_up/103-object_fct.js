#!/usr/bin/node

/**
 * This script is only to be updated.
 * The update is to add the function incr to increment the integer
 * The use of 'var' is prohibited
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () {
  this.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
