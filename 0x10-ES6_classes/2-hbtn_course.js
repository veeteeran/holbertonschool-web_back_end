class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (name) !== 'string') {
      throw TypeError('Name must be a string');
    } else if (typeof (length) !== 'number') {
      throw TypeError('Length must be a number');
    } else if (!Array.isArray(students) || (
      students.every((e) => typeof (e) !== 'string')
    )) {
      throw TypeError('Students must be an array of strings');
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof (newName) !== 'string') {
      throw TypeError('Name must be a string');
    }

    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof (newLength) !== 'number') {
      throw TypeError('Length must be a number');
    }

    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudent) {
    if (!Array.isArray(newStudent) || (
      newStudent.every((e) => typeof (e) !== 'string')
    )) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = newStudent;
  }
}

export default HolbertonCourse;
