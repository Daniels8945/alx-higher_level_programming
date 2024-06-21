#!/usr/bin/node

const myObject = { type: 'object', value: 12 };
console.log(myObject);
const myObject1 = { type: 'object', value: 89 };
Object.assign(myObject, myObject1);
console.log(myObject);
