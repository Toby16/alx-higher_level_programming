#!/usr/bin/node
const { argv } = require('process');
const numInt = Number(argv[2]);
let rValue = 1;

for (let i = 1; i <= numInt; i++) {
  rValue *= i;
}
console.log(rValue);
