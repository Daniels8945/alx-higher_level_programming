#!/usr/bin/node

const argc = [].length;
if (argc < 1) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else if (argc >= 2) {
  console.log('Arguments found');
}
