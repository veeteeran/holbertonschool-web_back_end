#!/usr/bin/node
const appendToEachArrayValue = (array, appendString) => {
    for (value of array) {
      value = appendString + value;
    }
  
    return array;
}
  
export default appendToEachArrayValue;