#!/usr/bin/node

const args = Number(process.argv[2]);

function factorial (args) {
  if (Number.isNaN(args) || args === 1) {
    return 1;
  } else {
    return (args * factorial(args - 1));
  }
}
console.log(factorial(args));
