#!/usr/bin/node

const argv = process.argv.slice(2);
let number = parseInt(argv[0]);

if (!argv[0]) {
  console.log('Missing number of occurrences');
} else if (isNaN(number) || number < 0) {
  process.exit(1);
} else {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
}
