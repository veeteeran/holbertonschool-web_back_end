import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    response.status(200);
    response.set('Content-Type', 'text/plain');
    readDatabase(process.argv[2])
      .then((value) => {
        response.write('This is the list of our students\n');
        response.write(`Number of students: ${value.lines.length}\n`);
        response.write(`Number of students in CS: ${value.cs.length}. List: ${value.cs.join(', ')}\n`);
        response.write(`Number of students in SWE: ${value.swe.length}. List: ${value.swe.join(', ')}`);
        response.end();
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    response.status(200);
    response.set('Content-Type', 'text/plain');
    readDatabase(process.argv[2])
      .then((value) => {
        const { major } = request.params;
        if (major === 'cs')
          response.send(`Number of students in CS: ${value.cs.length}. List: ${value.cs.join(', ')}`);
        else if (major === 'swe')
          response.send(`Number of students in SWE: ${value.swe.length}. List: ${value.swe.join(', ')}`);
        else {
          response.status(500);
          response.send('Major parameter must be CS or SWE');
        }
      })
      .catch((err) => {
        response.status(500);
        response.send(err.message);
      });
  }
}

module.exports = StudentsController;
