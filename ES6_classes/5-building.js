export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      this.evacuationWarningMessage();
    } else {
      this.sqft = sqft;
    }
  }

  get sqtf() {
    return this._sqtf;
  }

  set sqft(value) {
    this._sqtf = value;
  }

  /* eslint-disable */
  evacuationWarningMessage() {
    throw Error('Class extending Building must override evacuationWarningMessage');
  }
}
