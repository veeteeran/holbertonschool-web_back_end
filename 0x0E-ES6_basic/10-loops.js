#!/usr/bin/node
const appendToEachArrayValue = (array, appendString) => {
  for (const element of array) {
    array.shift();
    array.push(`${appendString}${element}`);
  }

  return array;
};

export default appendToEachArrayValue;
