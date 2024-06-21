#!/usr/bin/node

const args = process.argv.splice(2);

const x = parseInt(args[0]);

const square = 'X';

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += square;
    }
    console.log(row);
  }
}
