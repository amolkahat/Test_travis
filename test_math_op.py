import math_op
import unittest

class TestMathOP(object):


    def test_add_op():
        assert math_op.add(10, 20) == 30

    def test_mul_op():
        assert math_op.mul(10, 20) == 200

    def test_mul_op():
        assert math_op.mul(10, 20) == 20


if __name__ == '__main__':
    unittest.main()
