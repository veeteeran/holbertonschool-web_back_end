class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof(name) !== 'string') {
      throw TypeError('Name must be a string')
    } else if (typeof(length) !== 'number') {
      throw TypeError('Length must be a number')
    } else if (typeof (students !== 'object') || (
      students.every(e => typeof(e) !== 'string')
    )) {
      throw TypeError('Students must be an array of strings')
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set changeName(newName) {
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set changeLength(newLength) {
    this._length = newLength
  }

  get students() {
    return this._students;
  }

  set changeStudents(newStudent) {
    this._students.push(newStudent);
  }
}
  
export default HolbertonCourse;
