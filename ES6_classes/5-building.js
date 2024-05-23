export default class Building {
  constructor(sqft) {
    if (new.target !== Building) {
      this.evacuationWarningMessage();
    }
    this.sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }
  /* eslint-disable */
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
  /* eslint-disable */
}
