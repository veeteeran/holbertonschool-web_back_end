const cleanSet = (set, startString) => {
  if (startString === '') return '';
  if (set instanceof Set === false) return '';
  if (typeof startString !== 'string') return '';

  return [...set]
    .filter(s => s.startsWith(startString))
    .map(value => value.substring(startString.length))
    .join('-')
}

export default cleanSet;