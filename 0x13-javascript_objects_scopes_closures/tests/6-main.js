#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();
s1.charPrint('C');

const s2 = new Square();
console.log(s2);

const s3 = new Square(-2);
console.log(s3);

s1.charPrint('*');
s1.double();
s1.charPrint('+');
