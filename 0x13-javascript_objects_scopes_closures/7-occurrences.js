#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let no_occurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      no_occurrences++;
    }
  }
  return no_occurrences;
};
