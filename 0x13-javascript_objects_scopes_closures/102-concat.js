#!/usr/bin/node
const file = require('fs');

const fileArg = file.readFileSync(process.argv[2]).toString();
const sArg = file.readFileSync(process.argv[3]).toString();
file.writeFileSync(process.argv[4], fileArg + sArg);
