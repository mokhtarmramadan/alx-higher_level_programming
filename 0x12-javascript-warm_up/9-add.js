#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length !== 2 || !argv[0] || !argv[1]) {
  console.log('NaN');
} else {
  const firstNumber = parseInt(argv[0]);
  const secondNumber = parseInt(argv[1]);

  if (isNaN(firstNumber) || isNaN(secondNumber)) {
    console.log('NaN');
  } else {
    add(firstNumber, secondNumber);
  }
}

function add (a, b) {
  console.log(a + b);
}
