#!/usr/bin/node
const importedVal = require('./101-data.js');
const dictVal = importedVal.dict;

const newDict = {};
for (const key in dictVal) {
  if (newDict[dictVal[key]] === undefined) {
    newDict[dictVal[key]] = [];
  }
  newDict[dictVal[key]].push(key);
}
console.log(newDict);
