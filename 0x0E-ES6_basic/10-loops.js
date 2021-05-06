const appendToEachArrayValue = (array, appendString) => {
  let newArr = []
  for (const element of array) {
    newArr.push(`${appendString}${element}`);
  }

  return newArr;
};

export default appendToEachArrayValue;
