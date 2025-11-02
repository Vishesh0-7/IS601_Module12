from app import operations as ops
import math
import pytest

def test_add():
    assert ops.add(1, 2) == 3

def test_sub():
    assert ops.sub(5, 2) == 3

def test_mul():
    assert ops.mul(3, 4) == 12

def test_div_normal():
    assert ops.div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        ops.div(1, 0)

def test_float_precision():
    assert math.isclose(ops.add(0.1, 0.2), 0.30000000000000004)
