/** A script that updates the text of the <header> element to New Header!!!
 *  +when the user clicks on DIV#update_header
 *
 *  - document.querySelector cannot be used
 *  - JQuery API cannot be used
 */

$('document').ready(() => {
  $('div#update_header').click(() => {
    $('header').text('New content');
  });
});
