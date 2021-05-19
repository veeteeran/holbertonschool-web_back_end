const cleanSet = (set, startString) => {
  if (startString === '') return '';

  return [...set]
    .filter((s) => typeof s === 'string' && s.startsWith(startString))
    .map((value) => value.substring(startString.length))
    .join('-');
};

export default cleanSet;
