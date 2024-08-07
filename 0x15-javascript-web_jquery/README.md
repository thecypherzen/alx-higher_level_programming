# Overview #

Using *JavaScript* is awesome, but with it, you get to write too many lines of code for pretty simple tasks like simple DOM Elements selection. It gets with other tasks like toggling classnames, event handling and animations. [JQuery](https://api.jquery.com/), as a JS Library, makes life easier, given that we're able to do much with shorter lines of code. The good thing is - it's small - and can be imported using it's cdn link!


## Learning Objectives ##
It's expected that at the end of this project, the following one should understand:
- Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a GET request with JQuery Ajax
- How to make a POST request with JQuery Ajax
- How to listen/bind to DOM events

<br/><br/>
### General Requirements ###
- Allowed editors: vi, vim, emacs
- All files interpreted on Chrome (version 57.0)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory. Code should be `semistandard` compliant with the flag `--global $`: `semistandard *.js --global $`
- Must use JQuery version 3.x
- Not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data, etc

<br/><br/>
## Resources ##
- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
- [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
- [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
- [API](https://oscarotero.com/jquery/)
- [Introduction](https://jquery-tutorial.net/ajax/introduction/)
- [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
- [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
- [JQuery](https://jquery.com/)
- [JQuery API](https://api.jquery.com/)
- [JQuery Ajax](https://learn.jquery.com/ajax/)

<br/><br/>
### Dependencies ###
JQuery 3.x
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

<br/><br/>
### Project Timeline Details ###
- **Released:** Wed 7 Aug 2024 - 6am.
- **1st Deadline:** Thur 8 Aug 2024 - 6am.
- **Duration:** 24 hrs (1 day).
- **Author: **[William Inyam](https://github.com/thecypherzen/)

<br/><br/>
## Files ##
Files on the project are task based and are as follows:
| SN | File | Description |
|----|------|-------------|
| 1. |[0-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/0-script.js)  | A JavaScript script that updates the text color of the <header> element to red (#FF0000) using `document.querySelector` to select the HTML tag:<ul><li>test with [0-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/0-main.html).</li></ul>|
| 2. |[1-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/1-script.js) | JavaScript script that updates the text color of the <header> element to red (#FF0000) without using `document.querySelector` to select the HTML tag:<ul><li>test with [0-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/1-main.html).</li></ul>|
| 3. |[2-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/2-script.js) | A JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header without using `document.querySelector` to select the HTML tag:<ul><li>test with [1-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/2-main.html)</li>|
| 4. |[3-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/3-script.js) | A JavaScript script that adds the class red to the `<header>` element when the user clicks on the tag `DIV#red_header` without using `document.querySelector` to select the HTML tag. <ul><li>test with [3-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/3-main.html).</li></ul>|
| 5. |[4-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/4-script.js) | A JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header` without using `document.querySelector` to select the HTML tag. <ul><li>The `<header>` element must always have one class: *red* or *green*, never both in the same time and never empty.</li><li>If the current class is red, when the user click on `DIV#toggle_header`, the class must be updated to *green* ; and the reverse.</li></li><li>test with [4-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/4-main.html).</li></ul>|
| 6. |[5-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/5-script.js) |A JavaScript script that adds an `<li>` element to a list when the user clicks on the tag `DIV#add_item` without using `document.querySelector` to select the HTML tag. <ul><li>The new element must be: `<li>Item</li>`</li><li>The new element must be added to `UL.my_list`</li><li>test with [5-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/5-main.html).</li></ul>|
| 7. |[6-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/6-script.js) |A JavaScript script that updates the text of the `<header>`element to *New Header!!!*when the user clicks on `DIV#update_header` without using `document.querySelector` to select the HTML tag. <ul><li>test with [6-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/6-main.html).</li></ul> |
| 8. |[7-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/7-script.js) |A JavaScript script that fetches the *character name* from this *URL: https://swapi-api.alx-tools.com/api/people/5/?format=json* without using `document.querySelector` to select any HTML tag.<ul><li>The name must be displayed in the HTML tag `DIV#character`</li><li>must be imported from the `<head>` tag, not at the end of the HTML</li><li>test with [7-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/7-main.html).</li></ul>|
| 9. |[8-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/8-script.js) |A JavaScript script that fetches and lists the *title* for all movies by using this URL: *https://swapi-api.alx-tools.com/api/films/format=json* without using `document.querySelector` to select the HTML tag. <ul><li>All movie titles must be list in the HTML tag `UL#list_movies`</li><li>must be imported from the <head> tag, not at the end of the HTML</li><li>test with [8-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/8-main.html).</li></ul> |
| 10. |[9-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/9-script.js) |A JavaScript script that fetches from*https://hellosalut.stefanbohacek.dev/?lang=fr* and displays the value of *hello* from that fetch in the HTML tag `DIV#hello`. without using `document.querySelector` to select the HTML tag. <ul><li>The translation of “hello” must be displayed in the HTML tag `DIV#hello`</li><li>Must work when it is imported from the <head> tag</li><li>test with [9-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/9-main.html).</li></ul>|
| 11. |[100-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/100-script.js) |A JavaScript script that  that updates the text color of the <header> element to red (#FF0000) without using the JQuery API, and must use `document.querySelector` to select the HTML tag.<ul><li>must work when it is imported from the <head> tag</li><li>test with [100-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/100-main.html).</li></ul>|
| 12. |[101-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/101-script.js) |A JavaScript script that adds, removes and clears LI elements from a list when the user clicks:<ul><li>The new element must be: `<li>Item</li>`</li><li>The new element must be added to `UL.my_list`</li><li>When the user clicks on `DIV#add_item`, a new element is added to the list</li><li>When the user clicks on `DIV#remove_item`, the last element is removed from the list</li><li>When the user clicks on `DIV#clear_list`, all elements of the list are removed</li></ul>Constraints:<ul><li>can’t use `document.querySelector` to select the HTML tag</li><li>must use the JQuery API and</li><li>must work when imported in the `HEAD` tag.</li></ul>Test with [101-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/101-main.html)|
| 13. |[102-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/102-script.js) |A JavaScript script that fetches and prints how to say “Hello” depending on the language.<ul><li>uses this API service: *https://www.fourtonfish.com/hellosalut/hello/*</li><li>The language code will be the value entered in the tag `INPUT#language_code` (ex: es, fr, en etc.)</li><li>The translation is fetched when the user clicks on `INPUT#btn_translate`</li><li>The translation of “Hello” is displayed in the HTML tag `DIV#hello`</ul>Constraints:<ul><li>can’t use `document.querySelector` to select the HTML tag</li><li>must use the JQuery API and</li><li>must work when imported in the `HEAD` tag.</li></ul>Test with [102-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/102-main.html)|
| 14. |[103-script.js](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/103-script.js) |JavaScript script that fetches and prints how to say “Hello” depending on the language.<ul><li>extends [102-script.js]() to allow submission when user presses *Enter* key.</li><li>test with [103-main.html](https://github.com/thecypherzen/alx-higher_level_programming/blob/main/0x15-javascript-web_jquery/mainfiles/103-main.html)</li><ul>|
| 15. |README.md| Folder reame file  |
| 16. |[mainfiles](https://github.com/thecypherzen/alx-higher_level_programming/tree/main/0x15-javascript-web_jquery/mainfiles) | Folder of all html files for each script above. Each main file matches number pre-fix of the script name.<br/>Example:<br/>&nbsp;&nbsp;&nbsp;The script `2-script.js` has the corresponding html file `2-main.html`. |