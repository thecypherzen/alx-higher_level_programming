#!/usr/bin/node
/** A script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
 *  + and displays the value of hello from that fetch in the HTML tag DIV#hello.
 *
 *  - The translation of “hello” must be displayed in the HTML tag DIV#hello
 *  - document.querySelector cannot be used
 *  - JQuery API cannot be used
 *  - The script must work when it is imported from the <head> tag
 */

$('document').ready(() => {
  jQuery.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    (result) => {
      const val = result?.hello ?? "Error! No 'hello' attr in result.";
      $(`<p>${val}</p>`).appendTo('div#hello');
    }
  );
});
