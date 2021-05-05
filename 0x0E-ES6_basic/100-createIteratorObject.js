#!/usr/bin/node
const createIteratorObject = (report) => {
    let arr = [];
    for (let key in report) {
        arr.push(...report[key]);
    }

    return arr;
}

export default createIteratorObject