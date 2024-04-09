#!/usr/bin/node

/**
 * A script defining a function that converts a number from
 * +base 10 to another base passed as an argument
 * Declaring variables and using imports not allowed.
 */

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
