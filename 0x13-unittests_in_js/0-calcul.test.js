/* eslint-disable */
const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe('calculateNumber', () => {

        assert.strictEqual(calculateNumber(1, 1.5), 3);
        assert.strictEqual(calculateNumber(1.7, 1.5), 4);
        assert.strictEqual(calculateNumber('text', 1), NaN);
        assert.strictEqual(calculateNumber('text', 'str'), NaN);
        assert.strictEqual(calculateNumber(4, 4.8), 9);
        assert.ok(isNaN(calculateNumber(1, "str")));
        assert.ok(isNaN(calculateNumber("str", 1,2)));
        assert.ok(isNaN(calculateNumber("str", "str")));
});
