#!/usr/bin/node

const argv = process.argv.slice(2);

if (!argv[0]) {
  argv[0] = 'undefined';
} else if (!argv[1]) {
  argv[1] = 'undefined';
}

console.log(argv[0], 'is', argv[1]);
