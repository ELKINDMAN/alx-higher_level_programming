#!/usr/bin/node

const times = process.argv[2];
const intg = Number(times);

if (isNaN(intg)) {
	console.log('Missing number of occurences');
} else {
	let x;
	for (x = 1; x <= intg; x++) {
		console.log('C is fun');
	}
}
