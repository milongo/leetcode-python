from leetcode_python.stacks import is_valid  # Assuming your function is in a file named solution.py


def test_is_valid():
    assert is_valid("(){}[]") == True


def test_is_not_valid():
    assert is_valid("][]") == False
