#!/usr/bin/node

function add(a, b){
	return a + b;

console.log(add(a, b));
}

add(Number(process.argv[2]), Number(process.argv[3]));
