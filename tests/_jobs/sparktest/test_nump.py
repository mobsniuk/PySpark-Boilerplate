import numpy as np
import sys


def test_numpy():
    paths = '\n'.join(sys.path)
    print(paths)

    a = np.arange(6)
    expected = np.array([0, 1, 2, 3, 4, 5])
    np.testing.assert_array_equal(expected, a)
