#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const val = Number(process.argv[2]);
  let i = 0;
  while (i < val) {
    console.log('X'.repeat(val));
    i++;
  }
}
