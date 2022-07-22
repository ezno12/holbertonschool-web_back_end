export default function cleanSet(set, startString) {
  if (startString.length === 0 || typeof set !== 'object') return '';
  const res = [];
  for (const elem of set) {
    if (elem && elem.startsWith(startString)) {
      res.push(elem.replace(startString, ''));
    }
  }
  return res.join('-');
}
