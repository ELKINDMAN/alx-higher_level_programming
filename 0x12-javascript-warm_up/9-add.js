#!/usr/bin/node

const cmdVal = process.argv[2];
const cmdVal2 = process.argv[3];

function add(a, b) {
	console.log(a + b);
}

add(cmdVal, cmdVal2);
