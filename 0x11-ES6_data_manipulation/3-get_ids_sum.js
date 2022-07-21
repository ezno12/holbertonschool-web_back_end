export default function getStudentIdsSum(students) {
  return students.reduce((totalID, currentStudent) => totalID + currentStudent.id, 0);
}
