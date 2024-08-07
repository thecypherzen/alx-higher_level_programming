/** A script that adds the class red to the <header> element when the user
 *  +clicks on the tag DIV#red_header
 *
 *  document.querySelector cannot be used
 *  JQuery API must be used
 */

$('document').ready(() => {
  $('div#red_header').click(() => {
    $('header').addClass('red');
  });
});
