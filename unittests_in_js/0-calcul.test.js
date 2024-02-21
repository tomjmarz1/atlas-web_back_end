var calculateNumber = require('./0-calcul-0')

var assert = require('assert');

describe('calculateNumber', function () {
  it('should return result of adding rounded ', function () {
    assert.equal(calculateNumber(1.0, 3.2), 4);
    assert.equal(calculateNumber(1.2, 3.2), 4);
    assert.equal(calculateNumber(1.7, 3.2), 5);
  });
  it('should return result of adding rounded numbers', function () {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('should return result of adding rounded numbers', function () {
    assert.equal(calculateNumber(1.0, 3.7), 5);
  });
  
  it('should return result of adding rounded numbers', function () {
    assert.equal(calculateNumber(1.5, 3.7), 6);
    
  });
});