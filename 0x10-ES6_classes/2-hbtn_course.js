export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) !== 'string') throw TypeError('name must be a srting');
    if (typeof (length) !== 'number') throw TypeError('length must be a number');
    if (!Array.isArray(students)) throw TypeError('students must be an array');
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get getName() {
    return this._name;
  }

  set setName(name) {
    this._name = name;
  }

  get getLength() {
    return this._length;
  }

  set setLength(length) {
    this.length = length;
  }

  get getStudents() {
    return this._students;
  }

  set setStudents(students) {
    this._students = students;
  }
}
