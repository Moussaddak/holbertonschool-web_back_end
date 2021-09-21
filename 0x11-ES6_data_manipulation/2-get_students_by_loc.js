export default function getStudentsByLocation(arrayOfStudentIds, city) {
  return (Array.isArray(arrayOfStudentIds) && typeof city === 'string')
    ? arrayOfStudentIds.filter((student) => student.location === city) : [];
}
