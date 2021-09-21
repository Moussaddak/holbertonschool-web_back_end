export const weakMap = new WeakMap();
export function queryAPI(obj) {
  weakMap.set(obj, weakMap.get(obj) + 1 || 1);
  if (weakMap.get(obj) >= 5) {
    throw Error('Endpoint load is high');
  }
  return weakMap;
}
