import express from 'express';
import { getHomePage } from '../controllers/AppController';
import { getAllStudents, getAllStudentsByMajor } from '../controllers/StudentsController';

const router = express.Router();

router.get('/', getHomePage);
router.get('/students', getAllStudents);
router.get('/students/:major', getAllStudentsByMajor);

module.exports = router;