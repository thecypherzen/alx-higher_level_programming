#!/usr/bin/node
/** A JS script that updates the text color of the <header> element to red
 *  + (#FF0000):
 *
 *  - must use document.querySelector to select the HTML tag
 *  - JQuery API cannot be used
 *  - The script must work when it is imported from the <head> tag
 */

document.addEventListener('DOMContentLoded', () => {
  document.querySelector('header').style.color = '#FF0000';
});
