/* eslint-disable */
const assert = require('assert').strict;
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
});
