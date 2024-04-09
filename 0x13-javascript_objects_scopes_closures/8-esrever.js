#!/usr/bin/node

/**
 *  A function that reverses a list without using the 'reverse' method
 */

exports.esrever = function (list) {
  function swap (a, b) {
    const temp = list[a];
    list[a] = list[b];
    list[b] = temp;
  }
  let i, j;
  i = 0;
  j = list.length - 1;
  while (i < j) {
    swap(i, j);
    i++;
    j--;
  }
  return list;
};
