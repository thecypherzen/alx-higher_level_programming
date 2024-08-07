/** A script that adds, removes and clears LI elements from a list when
 *  + the user clicks on:
 *
 *  - DIV#add_item: a new element is added to the list
 *  - DIV#remove_item: the last element is removed from the list
 *  - DIV#clear_list: all elements of the list are removed
 *  - The new element must be: <li>Item</li>
 *  - The new element must be added to UL.my_list
 *  - Cannot use document.querySelector to select the HTML tag
 *  - JQuery API must be used
 *  - The script must work when it is imported from the <head> tag
 */

$('document').ready(() => {
  /* add item to list */
  $('div#add_item').click(() => {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  /* delete last child from list */
  $('div#remove_item').click(() => {
    $('ul.my_list li:last-child').remove();
  });

  /* clear list */
  $('div#clear_list').click(() => {
    $('ul.my_list').html('');
  });
});
