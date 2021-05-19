const cleanSet = (set, startString) => {
  if (startString === '') return '';

  return [...set]
    .filter(s => s.startsWith(startString))
    .map(value => value.substring(startString.length))
    .join('-')
}

export default cleanSet;