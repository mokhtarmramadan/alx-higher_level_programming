#!/usr/bin/node

const argv = process.argv.slice(2);
const number = parseInt(argv);

if (!argv[0] || isNaN(number)) {
  console.log('Missing size');
} else if (number > 0) {
  let asterisk = '';
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      asterisk += 'X';
    }
    console.log(asterisk);
    asterisk = '';
  }
}
