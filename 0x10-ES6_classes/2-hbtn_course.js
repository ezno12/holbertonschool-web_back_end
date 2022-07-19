export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) !== 'string') throw TypeError('name must be a srting');
    if (typeof (length) !== 'number') throw TypeError('length must be a number');
    for (const student in students) {
      if (typeof (student) !== 'string') throw TypeError('students must be a string');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) !== 'string') throw TypeError('name must be a srting');
    this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof (length) !== 'number') throw TypeError('length must be a number');
    this.length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    for (const student in students) {
      if (typeof (student) !== 'string') throw TypeError('students must be a string');
    }
    this._students = students;
  }
}
