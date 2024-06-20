#!/usr/bin/node

process.argc = [].length;
if (process.argc < 1) {
  console.log('No argument');
} else if (process.argc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
