const hasValuesFromArray = (set, array) => {
  let result = true;
  array.forEach(element => {
    if (!set.has(element)) {
      result = false;
      return;
    }
  });

  return result;
}

export default hasValuesFromArray;
