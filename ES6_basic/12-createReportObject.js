export default function createReportObject(employeesList) {
  const employeeObject = {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments: (employeesList) => Object.keys(employeesList).length,
  };
  return employeeObject;
}
