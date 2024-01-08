#!/usr/bin/node

const list = process.argv.slice(2);
if (!list || list.length === 0 || list.length === 1) {
  console.log('0');
  process.exit(1);
}
bubbleSort(list);
console.log(list[list.length - 2]);

function bubbleSort (list) {
  const listLength = list.length;
  for (let i = 0; i < listLength - 1; i++) {
    for (let j = 0; j < listLength - 1 - i; j++) {
      if (list[j] > list[j + 1]) {
        const temp = list[j];
        list[j] = list[j + 1];
        list[j + 1] = temp;
      }
    }
  }
}
