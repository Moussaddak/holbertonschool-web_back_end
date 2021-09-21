/*eslint-disable */

export default function getListStudentIds(array) {
    return Array.isArray(array) ? array.map((item) => item.id) : [];
}
// export default arr => Array.isArray(arr) && arr.map(item => item.id) || [];
