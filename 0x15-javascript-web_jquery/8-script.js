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
      let results = result.results;
      /* console.log(results); */
      results = results.map((film) => {
        return film.title;
      });
      results.forEach(title => {
        $(`<li>${title}</li>`).appendTo('ul#list_movies');
      });
    }
  );
});
