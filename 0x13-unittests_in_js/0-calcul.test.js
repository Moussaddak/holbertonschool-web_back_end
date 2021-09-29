/* eslint-disable */
const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe('calculateNumber', () => {

        assert.equal(calculateNumber(1, 1.5), 3);
        assert.equal(calculateNumber(1.7, 1.5), 4);
        assert.equal(calculateNumber('text', 1), NaN);
        assert.equal(calculateNumber('text', 'str'), NaN);
        assert.strictEqual(calculateNumber(4, 4.8), 9);
        assert.ok(isNaN(calculateNumber(1, "str")));
        assert.ok(isNaN(calculateNumber("str", 1,2)));
        assert.ok(isNaN(calculateNumber("str", "str")));
});
