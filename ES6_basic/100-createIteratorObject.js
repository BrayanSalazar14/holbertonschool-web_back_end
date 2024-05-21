export default function createIteratorObject(report) {
  const employeesName = [];
  for (const data of Object.values(report.allEmployees)) {
    for (const employee of data) {
      employeesName.push(employee);
    }
  }
  return employeesName;
}
