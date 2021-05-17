const cleanSet = (set, startString) => {
  let result = '';

  if (startString === '') return result;

  set.forEach(s => {
    if (s.startsWith(startString)) {
      if (result === '') {
        result += s.substring(startString.length);
      } else {
        result += `-${s.substring(startString.length)}`;
      }
    }
  })

  return result;
}

export default cleanSet;