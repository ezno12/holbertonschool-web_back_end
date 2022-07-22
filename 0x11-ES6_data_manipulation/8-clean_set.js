export default function cleanSet(set, startString) {
  const res = [];
  for (const elem of set) {
    if (elem && elem.startsWith(startString)) {
      res.push(elem.replace(startString, ''));
    }
  }
  return res.join('-');
}
