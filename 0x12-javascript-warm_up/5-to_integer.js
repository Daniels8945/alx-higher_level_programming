#!/usr/bin/node

const args = process.argv.splice(2);

if (+args) {
  console.log('My number: ' + Math.round(args[0]));
} else if (typeof args[0] === 'string') {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
