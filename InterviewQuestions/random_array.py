import random

import pytest


def randomize_array(n=10):
    return [random.randint(0, 10) for _ in range(n)]


def test_randomize_array(n=10):
    print("\n", randomize_array(n))
    assert len(randomize_array(n)) == n
    assert len(randomize_array(0)) == 0


if __name__ == '__main__':
    print(f"\n Running tests for {__file__}...")
    pytest.main([__file__])