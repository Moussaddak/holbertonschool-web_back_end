export default function appendToEachArrayValue(array, appendString) {
    const tab = [];
    for (const value of array) {
        tab.push(`${appendString}${value}`);
    }

    return tab;
}
