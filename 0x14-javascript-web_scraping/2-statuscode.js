#!/usr/bin/node

/* using request module instead - checker requirement */

const request = require('request');

const URL = String(process.argv[2]);

request(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

/*
const fetch = require('node-fetch');

(async () => {
  const URL = String(process.argv[2]);

  const response = await fetch(URL);

  console.log('code: ' + response.status);
})();
*/
