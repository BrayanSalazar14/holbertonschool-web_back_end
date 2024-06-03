export default function hasValuesFromArray(set, array) {
  const results = array.map((element) => set.has(element));
  if (results.includes(false)) return false;
  return true;
}
