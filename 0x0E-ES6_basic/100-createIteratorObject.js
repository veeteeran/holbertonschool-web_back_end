#!/usr/bin/node
const createIteratorObject = (report) => {
  const { allEmployees } = report;
  const arr = [];

  for (const key in allEmployees) {
    arr.push(...allEmployees[key]);
  }
  return arr;
};

export default createIteratorObject;
