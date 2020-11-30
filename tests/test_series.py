from math_series.series import fibonacci,lucas,sum_series

"""
test 
base 0, >> 0
base 1, >> 1
number 6 >> fibonacci(n-1) + fibonacci(n-2)
string >> invalid type

"""

def test_f_zero():
    actual = fibonacci(0)
    expected = 0
    assert expected == actual

def test_f_one():
    actual = fibonacci(1)
    expected = 1
    assert expected == actual

def test_f_six():
    actual = fibonacci(6)
    expected = 8
    assert expected == actual

def test_invalid_type_f():
    actual = fibonacci('hi')
    expected = 'invalid input'
    assert expected == actual

"""
test 
base 0, >> 2
base 1, >> 1
number 3 >> fibonacci(n-1) + fibonacci(n-2)
string >> invalid type

"""


def test_l_zero():
    actual = lucas(0)
    expected = 2
    assert expected == actual

def test_l_one():
    actual = lucas(1)
    expected = 1
    assert expected == actual

def test_l_three():
    actual = lucas(3)
    expected = 4
    assert expected == actual

def test_invalid_type_l():
    actual = lucas('hi')
    expected = 'invalid input'
    assert expected == actual


"""
test 
base 0, >> first
base 1, >> second
number 3 >> sum_series(n-1,first,second) + sum_series(n-2,first,second)
string >> invalid type

"""

def test_sum_zero_f():
    actual = sum_series(0)
    expected = 0
    assert expected == actual

def test_sum_one_f():
    actual = sum_series(1)
    expected = 1
    assert expected == actual

def test_sum_three_f():
    actual = sum_series(3)
    expected = 2
    assert expected == actual

def test_sum_zero_l():
    actual = sum_series(0,2,1)
    expected = 2
    assert expected == actual

def test_sum_one_l():
    actual = sum_series(1,2,1)
    expected = 1
    assert expected == actual

def test_sum_three_l():
    actual = sum_series(3,2,1)
    expected = 4
    assert expected == actual

def test_invalid_type_sum():
    actual = sum_series('hi')
    expected = 'invalid input'
    assert expected == actual

def test_invalid_type_sum_first():
    actual = sum_series(1,'hi',1)
    expected = 'invalid input'
    assert expected == actual

def test_invalid_type_sum_second():
    actual = sum_series(1,2,'1')
    expected = 'invalid input'
    assert expected == actual




