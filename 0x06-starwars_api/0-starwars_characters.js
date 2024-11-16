#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

request(
  'https://swapi.dev/api/films/' + movieId + '/',
  function (err, res, body) {
    if (err) throw err;

    const actors = JSON.parse(body).characters;

    const exactOrder = (actors, index) => {
      if (index === actors.length) return;

      request(actors[index], function (err, res, body) {
        if (err) throw err;

        console.log(JSON.parse(body).name);

        exactOrder(actors, index + 1);
      });
    };

    exactOrder(actors, 0);
  }
);
