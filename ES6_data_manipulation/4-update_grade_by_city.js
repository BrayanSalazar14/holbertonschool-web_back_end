export default function updateStudentGradeByCity(array, city, newGrades) {
  return array
    .filter((student) => student.location === city)
    .map((student) => {
      /* eslint-disable */
      const newGrade = newGrades.find((grade) => grade.studentId === student.id);
      student.grade = newGrade ? newGrade.grade : 'N/A';
      return student;
    });
}
