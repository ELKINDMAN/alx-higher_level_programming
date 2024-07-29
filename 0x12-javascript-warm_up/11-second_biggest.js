#!/usr/bin/node

const num = process.argv;
const newArray = [];

if (num.length === 3 || num[2] === undefined) {
	console.log(0);
} else {
	function iteratearr (num) {
		let i;
		for (i = 2; i < num.length; i++) {
			newArray.push(Number(num[i]));
		}
	}

	function sortArr (num) {
		const sorted =num.slice().sort((a, b) => a - b);
		return sorted;
	}
	function secondBiggest (sortedArray) {
		let i, least;
		for (i = 0; i < sortedArray.length - 1; i++) {
			least = i;
		}
		console.log(sortedArray[least]);
	}
	iteratearr(num);
	const sort = sortArr(newArray);
	secondBiggest(sort);
}
