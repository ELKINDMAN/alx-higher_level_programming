#!/usr/bin/node

const size = process.argv[2];
const intg = Number(size);


if (isNaN(intg)) {
	console.log('Missing size');
} else {
	for (let y = 0; y < intg; y++) {
		let row = '';
		for (let x = 0; x < intg; x++)
		{
			row += 'X';
		}
		console.log(row);
	}
}
