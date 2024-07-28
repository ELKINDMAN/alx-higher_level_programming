#!/usr/bin/node

const myarg = process.argv.length;
if (myarg === 3 ) {
	console.log('Argument found');
} else if (myarg > 3) {
	console.log('Arguments found');
} else {
	console.log('No argument');
}
