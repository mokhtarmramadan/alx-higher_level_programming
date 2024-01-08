#!/usr/bin/node

const argv = process.argv.slice(2);
const number = parseInt(argv);

if (isNaN(number) || !argv[0]) {
  console.log('1');
} else {
  const result = factorial(number);
  console.log(result);
}

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
