/*eslint-disable */
export default function updateUniqueItems(f) {
  if (!(f instanceof Map)) {
    throw Error('Cannot process');
  }
  f.forEach((value, key) => {
    value === 1 ? f.set(key, 100) : f.set(key, value);
  });
  return f;
}
