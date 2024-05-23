export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      this.evacuationWarningMessage();
    } else {
      this._sqft = sqft;
    }
  }

  get sqtf() {
    return this._sqtf;
  }

  /* eslint-disable */
  evacuationWarningMessage() {
    throw Error('Class extending Building must override evacuationWarningMessage');
  }
}
