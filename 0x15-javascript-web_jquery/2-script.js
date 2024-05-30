#!/usr/bin/node
/** A script that updates the text color of the <header> element to
 *  +red (#FF0000) when the user clicks on the tag DIV#red_header
 *
 *  document.querySelector cannot be used
 *  JQuery API must be used
 */

$('document').ready(() => {
  $('div#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
