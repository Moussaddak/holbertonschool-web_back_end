export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](value) {
    if (value === 'number') return this._size;
    if (value === 'string') return this._location;
    return null;
  }
}
