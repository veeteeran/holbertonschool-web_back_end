#!/usr/bin/node
import getBudgetObject from './7-getBudgetObject.js';

const getFullBudgetObject = (income, gdp, capita) => {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars: function (income) {
      return `$${income}`;
    },
    getIncomeInEuros: function (income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}

export default getFullBudgetObject;