export default function hasValuesFromArray(set, array) {
  array.forEach((element) => set.has(element));
}
