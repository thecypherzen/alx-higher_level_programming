#!/usr/bin/node

/**
 * A script that defines a function increments and calls a function.
 * The function is exported and made available to requiring modules.
 */

function countFunc (count, func) {
  count += 1;
  func(count);
  return (count);
}

module.exports.addMeMaybe = countFunc;
