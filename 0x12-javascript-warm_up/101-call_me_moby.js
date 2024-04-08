#!/usr/bin/node

/**
 * A script that executes a function n times
 * The function is exported and made available to requring modules
 */

function myFunc (n, func) {
  while (n > 0) {
    func();
    n--;
  }
}

module.exports.callMeMoby = myFunc;
