#!/usr/bin/node
const { argv } = require('process');
const argCount = argv.length - 2;

if (argCount <= 1) {
  console.log(0);
} else {
  const lst = [];
  for (let i = 0; i < argCount; i += 1) {
    // You can assume all arguments can be converted to integer
    lst[i] = Number(argv[i + 2]);
  }
  lst.sort((a, b) => b - a);
  console.log(lst[1]);
}
