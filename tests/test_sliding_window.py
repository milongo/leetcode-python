# test_max_subarray.py
import pytest
from leetcode_python.sliding_window import max_sum_subarray


@pytest.fixture
def example1():
    return {"arr": [2, 3, 4, 1, 5], "k": 2, "expected": 7}


@pytest.fixture
def example2():
    return {"arr": [2, 8, 4, 3, 1, 3], "k": 3, "expected": 15}


@pytest.fixture
def example3():
    return {"arr": [2, 1, 5, 1, 3, 2], "k": 3, "expected": 9}


@pytest.fixture
def example4():
    return {"arr": [10, 11, 12, 13, 14, 15], "k": 2, "expected": 29}


@pytest.fixture
def example5():
    return {"arr": [9, 11, 2, 3, 4, 5], "k": 4, "expected": 25}


@pytest.fixture
def edge_case():
    return {"arr": [1, 2, 3], "k": 5, "expected": -1}


def test_example1(example1):
    result = max_sum_subarray(example1["arr"], example1["k"])
    assert result == example1["expected"]


def test_example2(example2):
    result = max_sum_subarray(example2["arr"], example2["k"])
    assert result == example2["expected"]


def test_example3(example3):
    result = max_sum_subarray(example3["arr"], example3["k"])
    assert result == example3["expected"]


def test_example4(example4):
    result = max_sum_subarray(example4["arr"], example4["k"])
    assert result == example4["expected"]


def test_example5(example5):
    result = max_sum_subarray(example5["arr"], example5["k"])
    assert result == example5["expected"]


def test_edge_case(edge_case):
    result = max_sum_subarray(edge_case["arr"], edge_case["k"])
    assert result == edge_case["expected"]
