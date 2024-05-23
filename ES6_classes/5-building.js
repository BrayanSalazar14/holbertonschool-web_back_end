export default class Building {
  constructor(sqft) {
    if (new.target !== Building) {
      this.evacuationWarningMessage();
    } else {
      this._sqft = sqft;
    }
  }

  get sqtf() {
    return this.sqtf;
  }

  /* eslint-disable */
  evacuationWarningMessage() {
    throw Error('Class extending Building must override evacuationWarningMessage');
  }
}

// const b = new Building(100);
// console.log(b);

// class TestBuilding extends Building {}

// try {
//     new TestBuilding(200)
// }
// catch(err) {
//     console.log(err);
// }