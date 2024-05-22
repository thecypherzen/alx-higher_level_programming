#!/usr/bin/node

/*
const numbers = [0, 1, 2, 3, 4, 5, 6];
console.log(numbers.reduce(
    (a, b) => { console.log(a, b);
		   return a + b ;
		 }, 0
));
*/
myobj = {};
console.log(myobj['1'] || 0);
myobj['1'] = 5;
console.log(myobj['1'] || 0);
console.log(parseInt(true));
