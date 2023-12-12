#!/usr/bin/node
exports.esrever = function (list) {
  let myLength = list.length - 1;
  let i = 0;
  while ((myLength - i) > 0) {
    const a = list[myLength];
    list[myLength] = list[i];
    list[i] = a;
    i++;
    myLength--;
  }
  return list;
};
