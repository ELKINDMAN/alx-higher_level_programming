#!/usr/bin/node

const argline = process.argv[2];
const nanconvt = Number(argline);

if (isNaN(nanconvt)) {
	        console.log('Not a number');
} else if (typeof nanconvt === 'number') {
	        console.log('My number: ' + Number(nanconvt));
}
