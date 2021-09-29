/* eslint-disable */
const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe('calculateNumber', () => {
    it('when inputs are one float and other int', () => {
        assert.equal(calculateNumber(1, 1.5), 3);
    });
    it('when inputs are two float', () => {
        assert.equal(calculateNumber(1.7, 1.5), 4);
    });
    it('when inputs are one int and other str', () => {
        assert.equal(calculateNumber('text', 1), NaN);
    });
    it('when inputs are two string', () => {
        assert.equal(calculateNumber('text', 'str'), NaN);
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
