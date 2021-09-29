/* eslint-disable */
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('Test calculateNumber', () => {
    it('when inputs are one float and other int', () => {
        const result = calculateNumber(1, 1.5);
        assert.equal(result, 3);
    });
    it('when inputs are two float', () => {
        const result = calculateNumber(1.7, 1.5);
        assert.equal(result, 4);
    });
    it('when inputs are one int and other str', () => {
        const result  = calculateNumber('text', 1);
        assert.equal(result, NaN);
    });
    it('when inputs are two string', () => {
        const result = calculateNumber('text', 'str');
        assert.equal(result, NaN);
    });
    it('Test should return 9 when inputs are 4 et 4.8', () =>
        assert.strictEqual(calculateNumber(4, 4.8), 9));

    it('Test should return NAN when second argument is typeof String', () =>
        assert.ok(isNaN(calculateNumber(1, "str"))));
    it('Test should return NAN when first arg is typeof String', () =>
        assert.ok(isNaN(calculateNumber("str", 1,2))));
    it('Test should return NAN when both arguments are typeof String', () =>
        assert.ok(isNaN(calculateNumber("str", "str"))));
});
