#!/usr/bin/node

const { argv } = require('node:process');

if (process.argv.length > 2) {
	  console.log('Argument found');
} else {
	  console.log('No argument');
}
