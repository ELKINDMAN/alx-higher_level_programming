#!/usr/bin/node

const Rectangle = require('./4-rectangle');

const Square extends Rectangle = {
	constructor (size) {
		super(size, size);
	}
}
module.exports = Square;
