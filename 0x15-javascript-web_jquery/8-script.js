/** A script that fetches and lists the title for all movies by using this
 *  + URL: https://swapi-api.alx-tools.com/api/films/?format=json
 *
 *  - All movie titles must be listed in the HTML tag UL#list_movies
 *  - document.querySelector cannot be used
 *  - JQuery API cannot be used
 */

$('document').ready(() => {
  jQuery.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    (result) => {
      result.results.map((film) => {
        console.log(film);
        $(`<li>${film.title}</li>`).appendTo('ul#list_movies');
        return null;
      });
    });
});
