def add(x, y):
    return x + y


def test_small_numbers():
    assert add(2, 7) == 9, "The number sums is incorrect"


def test_big_numbers():
    assert add(125, 371) == 96, "The number sums is incorrect"