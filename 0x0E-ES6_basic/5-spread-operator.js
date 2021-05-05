const concatArrays = (array1, array2, string) => {
    const arr = [];
    return arr.push(...array1, ...array2, ...string);
};

export default concatArrays;