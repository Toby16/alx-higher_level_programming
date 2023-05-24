#!/usr/bin/node

const fetch = require('node-fetch');

(async () => {
  const URL = String(process.argv[2]);

  const response = await fetch(URL);

  console.log('code: ' + response.status);
})();
