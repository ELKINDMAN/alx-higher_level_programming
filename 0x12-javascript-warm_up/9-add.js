#!/usr/bin/node

const cmdVal = Number(process.argv[2]);
const cmdVal2 = Number(process.argv[3]);

function add(a, b) {
	console.log(a + b);
}

add(cmdVal, cmdVal2);
