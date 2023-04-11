#!/usr/bin/node
const { argv } = require('process');
const ArgLen = argv.length - 2;

if (ArgLen === 0) {
  console.log('No arguument');
} else if (ArgLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
