export default function cleanSet(set, startString) {
  try {
    return [...set]
      .filter((item) => typeof item === 'string' && item.startsWith(startString))
      .map((item) => item.replace(startString, ''))
      .join('-');
  } catch (e) {
    return '';
  }
}
