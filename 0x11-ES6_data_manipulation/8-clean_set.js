export default function cleanSet(set, startString) {
  if (startString === '') return '';

  try {
    return [...set]
      .filter((item) => typeof item === 'string' && item.startsWith(startString))
      .map((item) => item.slice(startString.length))
      .join('-');
  } catch (e) {
    return '';
  }
}
