export default function getStudentIdsSum(array) {
  return array.reduce((total, property) => total + property.id, 0);
}
