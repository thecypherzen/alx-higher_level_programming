#!/usr/bin/node
/** A script that fetches and prints how to say “Hello” depending on
 *  +the language
 *
 *  - api service to use: https://www.fourtonfish.com/hellosalut/hello/
 *  - The language code will be the value entered in the tag
 *    + INPUT#language_code (ex: es, fr, en etc.)
 *  - The translation must be fetched when the user clicks on
 *    + INPUT#btn_translate
 *  - The translation of “Hello” must be displayed in the HTML tag DIV#hello
 *  - Cannot use document.querySelector to select the HTML tag
 *  - JQuery API must be used
 *  - The script must work when it is imported from the <head> tag
 *  Note:
 *  As at now, https://www.fourtonfish.com/hellosalut/hello/ is moved
 *  + permanently to https://hellosalut.stefanbohacek.dev/ hence, the new
 *  + location url is used in this code.
 */

$('document').ready(() => {
  const translate = $('#btn_translate');
  const code = $('#language_code');

  // place request and handle success/failure
  translate.click(() => {
    jQuery.get(
            `https://hellosalut.stefanbohacek.dev/?lang=${code.val()}`,
            (success) => {
              const val = success?.hello ?? 'Error: Not supported.';
              $('#hello').html(`<p>${val}</p>`);
            }).fail((error) => {
      console.log(error.statusText);
    });
  });
});
