#!/usr/bin/node
/** A script that adds a <li> element to a list when the user clicks on the
 *  + tag DIV#add_item
 *
 *  - The new element must be: <li>Item</li>
 *  - The new element must be added to UL.my_list
 *  - document.querySelector cannot be used
 *  - JQuery API must be used
 */

$('document').ready(() => {
  $('div#add_item').click(() => {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
});
