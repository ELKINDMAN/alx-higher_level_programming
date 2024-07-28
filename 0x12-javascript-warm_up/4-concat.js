#!/usr/bin/node

const my_arg = process.argv[2];
const my_arg2 = process.argv[3];
const midchar = 'is';
const whsp = ' ';
if (my_arg !== undefined) {
	console.log(my_arg + whsp + midchar + whsp + my_arg2);
} else {
	console.log('undefined');
}
