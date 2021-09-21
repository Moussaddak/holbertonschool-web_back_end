/* eslint-disable */
export default function updateStudentGradeByCity(arrayOfStudentObjs, city, newGrades) {
    if (Array.isArray(arrayOfStudentObjs) && typeof newGrades === 'object' && typeof city === 'string') {
        const students = arrayOfStudentObjs.filter((obj) => obj.location === city);

        students.forEach((student) => {
            const objFound = newGrades.find((obj) => obj.studentId === student.id);
            objFound ? student.grade = objFound.grade : student.grade = 'N/A';
        });
        return students;
    }
    return [];
}
