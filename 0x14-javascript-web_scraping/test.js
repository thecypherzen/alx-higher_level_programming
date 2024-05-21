#!/usr/bin/node

/*
const numbers = [0, 1, 2, 3, 4, 5, 6];
console.log(numbers.reduce(
    (a, b) => { console.log(a, b);
		   return a + b ;
		 }, 0
));
*/

function myfunc(a,b,c){
    console.log(arguments, typeof(arguments));
}


myfunc(1,2,3)
