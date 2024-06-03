export default function getStudentsByLocation(array, city) {
  return array.filter((element) => element.location === city);
}
