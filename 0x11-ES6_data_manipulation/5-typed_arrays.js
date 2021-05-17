const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer);

  if (position > length - 1) throw Error('Position outside range');

  try {
    int8View[position] = value;
  } catch (e) {
    console.logerror(e);
  }

  return buffer;
};

export default createInt8TypedArray;
