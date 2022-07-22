export default function updateUniqueItems(myMap) {
  if (myMap instanceof Map === false) {
    throw new Error('Cannot process');
  }
  for (const [k, v] of myMap) {
    if (v === 1) myMap.set(k, 100);
  }
}
