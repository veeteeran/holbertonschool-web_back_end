import Car from './10-car'

class EVCar extends Car {
  constructor(brand, motor, color, range) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this._range = range;
  }

  static get [Symbol.species]() { return Car; }
}

export default EVCar;