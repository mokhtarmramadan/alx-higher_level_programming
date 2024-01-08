#!/usr/bin/node

const argv = process.argv.slice(2);
const argvNumber = argv.length;
if (argvNumber === 0) {
  console.log('No argument');
} else if (argvNumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
