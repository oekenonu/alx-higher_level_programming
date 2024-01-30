#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
req.get(url + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const dc = JSON.parse(body).characters;
  for (const i of dc) {
    req.get(i, function (err, res, bodi) {
      if (err) {
        console.log(err);
      }
      const d = JSON.parse(bodi);
      console.log(d.name);
    });
  }
});
