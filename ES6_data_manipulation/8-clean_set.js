export default function cleanSet(set, startString) {
  if (!(startString instanceof String)) return '';
  const newString = [];
  set.forEach((element) => {
    if (element.startsWith(startString)) newString.push(element.slice(startString.length));
  });
  return newString.join('-');
}
