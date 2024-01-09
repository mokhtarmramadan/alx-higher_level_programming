#!/usr/bin/node

const supSquare = require('./5-square.js');
class Square extends supSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        let c = 'C';
        for (let j = 0; j < this.width; j++) {
          c += 'C';
        }
        console.log(c);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
