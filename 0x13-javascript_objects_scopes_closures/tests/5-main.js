#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

const s2 = new Square(-1);
s2.print();
console.log(s2.width);
console.log(s2.height);
