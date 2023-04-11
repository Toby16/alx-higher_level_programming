#!/usr/bin/node
const { argv } = require('process');
const numInt = Number(argv[2]);

if (isNaN(numInt)) {
  console.log('Missing number of occurrences');
} else if (typeof numInt === 'number') {
  if (numInt > 0) {
    for (let i = 0; i < numInt; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
