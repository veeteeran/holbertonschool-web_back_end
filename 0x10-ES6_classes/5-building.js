class Building {
  constructor(sqft) {
    this._sqft = sqft;

    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(newSqft) {
    this._sqft = newSqft;
  }
}

export default Building;
