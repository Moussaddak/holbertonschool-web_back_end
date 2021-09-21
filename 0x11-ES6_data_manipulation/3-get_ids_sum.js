export default function getStudentIdsSum(arrayOfStudentObjs) {
  return Array.isArray(arrayOfStudentObjs)
    ? arrayOfStudentObjs.reduce((preValue, Value) => preValue + Value.id, 0) : 0;
}
