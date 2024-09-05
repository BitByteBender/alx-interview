#!/usr/bin/node
/* Star Wars Characer - The movie */

const req = require('request');
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

req(baseUrl, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.error('status code issue:', res.statusCode);
    return;
  }

  charsChecker(JSON.parse(body).characters, 0);
});

function charsChecker(chars, idx) {
  if (idx >= chars.length) {
    return;
  }

  req(chars[idx], (err, res, body) => {
    if (err) {
      console.error('Error:', err);
    } else if (res.statusCode === 200) {
      console.log(JSON.parse(body).name);
    } else {
      console.error('Status code wrong:', res.statusCode);
    }
    charsChecker(chars, idx + 1);
  });
}
