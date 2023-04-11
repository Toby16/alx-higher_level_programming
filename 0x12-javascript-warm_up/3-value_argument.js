#!/usr/bin/node
const { argv } = require('process');

const firstArg = argv[2];

if (firstArg === undefined) {
  console.log('Not argument');
} else {
  console.log(firstArg);
}
