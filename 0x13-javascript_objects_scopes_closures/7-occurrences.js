#!/usr/bin/node

/**
 * A script that counts the number of occurences of a value
 * +in an array
 */

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((elem) => {
    if (elem === searchElement) { count += 1; }
  });
  return count;
};
