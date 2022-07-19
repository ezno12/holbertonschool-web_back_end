import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    if (typeof (sqft) !== 'number' || typeof (floors) !== 'number') throw TypeError('must be a number');
    super(sqft);
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Eacuate slowly the ${this._floors} floors`;
  }
}
