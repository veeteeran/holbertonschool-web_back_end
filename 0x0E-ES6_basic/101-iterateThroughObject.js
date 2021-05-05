#!/usr/bin/node
const iterateThroughObject = (reportWithIterator) => {
    for (let i = 0; i < reportWithIterator.length; i++) {
        i < reportWithIterator.length - 1 ? console.log(`${reportWithIterator[i]} | `) : console.log(reportWithIterator[i]);
    }
}

export default iterateThroughObject;