#!/usr/bin/node

const argv = process.argv.slice(2);
const number = parseInt(argv[0]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ', number);
}
