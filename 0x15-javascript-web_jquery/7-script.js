/** A script that fetches the character name from this URL:
 *  + https://swapi-api.alx-tools.com/api/people/5/?format=json
 *
 *  - The name must be displayed in the HTML tag DIV#character
 *  - document.querySelector cannot be used
 *  - JQuery API cannot be used
 */

$('document').ready(() => {
  jQuery.get(
    'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    (result) => {
      $(`<p>${result.name}</p>`).appendTo('div#character');
    }
  );
});
