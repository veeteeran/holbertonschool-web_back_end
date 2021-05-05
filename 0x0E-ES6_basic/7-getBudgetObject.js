#!/usr/bin/node
const getBudgetObject = (income, gdp, capita) => {
    const budget = { income, gdp, capita };
    return budget;
};

export default getBudgetObject;