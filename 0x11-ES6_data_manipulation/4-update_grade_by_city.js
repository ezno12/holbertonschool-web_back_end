export default function updateStudentGradeByCity(students, city, newGrades) {
  students.filter((student) => student.location === city)
    .map((item) => {
      const newRecord = { ...item };

      const newStudent = newGrades.find((student) => student.studentId === item.id);

      if (newStudent) newRecord.grade = newStudent.grade;
      else newRecord.grade = 'N/A';
      return newRecord;
    });
}
