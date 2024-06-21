#!/usr/bin/node

const args = process.argv.splice(2);

function add (a, b) {
  const args1 = +args[a = 0];
  const args2 = +args[b = 1];

  return args1 + args2;
}
console.log(add());
