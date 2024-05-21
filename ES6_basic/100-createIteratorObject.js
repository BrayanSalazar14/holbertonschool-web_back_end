export default function createIteratorObject(report) {
  const i = [];
  for (const a of Object.values(report.allEmployees)) {
    for (const e of a) {
      i.push(e);
    }
  }
  return i;
}
