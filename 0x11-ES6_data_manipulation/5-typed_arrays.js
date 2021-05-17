const createInt8TypedArray = (length, position, value) => {
  let buffer = new ArrayBuffer(length);
  let int8View = new Int8Array(buffer, position, value);

  if (position > length - 1) {
    throw 'Position outside range'
  } else {
    int8View[position] = value;
  }

  return buffer;
}
