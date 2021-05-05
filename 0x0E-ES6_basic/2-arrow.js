#!/usr/bin/node
const getNeighborhoodsList = () => {
    this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
  
    const self = this;
    this.addNeighborhood = newNeighborhood => {
      self.sanFranciscoNeighborhoods.push(newNeighborhood);
      return self.sanFranciscoNeighborhoods;
    };
}
  
export default getNeighborhoodsList;