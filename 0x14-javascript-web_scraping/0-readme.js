#!/usr/bin/node
const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(
  argv[0],
  function (err, data) {
    if (err) {
      return console.error(err);
    }

    const lines = data.toString().split('\n');
    if (lines.length > 0) {
      console.log(lines[0]);
    } else {
      console.log('File is empty.');
    }
  }
);
