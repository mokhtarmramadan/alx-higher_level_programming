#!/usr/bin/node

exports.esrever = function (list) {
  const halfLength = parseInt(list.length / 2);
  for (let i = 0; i < halfLength; i++) {
    const j = list.length - 1 - i;
    swap(i, j, list);
  }
  return list;
};

function swap (i, j, list) {
  const temp = list[i];
  list[i] = list[j];
  list[j] = temp;
}
