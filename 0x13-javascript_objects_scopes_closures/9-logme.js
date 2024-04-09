#!/usr/bin/node

/**
 *  A script defining a function that prints the number of arguments
 *  +already printed and the new argument value in the format:
 *  '<number arguments already printed>: <current argument value>'
 *  Example:
 *     logMe("Hello"); => 0: Hello
 *     logMe("Best"); => 1: Best
 */

let count;

count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
