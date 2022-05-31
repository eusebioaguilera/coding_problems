import enum
import unittest


def optimize_box_weights(input_list):
    """
        Sort list by weight (greater first), and pop items until sum of box A is greater than B
    """
    B = list(input_list)
    B.sort(reverse=True)

    A = list()

    while True:
        if sum(A) > sum(B):
            break
        A.insert(0, B.pop(0))

    B.reverse()
    return A, B


class TestFindSumOfTwo(unittest.TestCase):
    def test1(self):
        self.assertEqual(optimize_box_weights(
            [3, 7, 5, 6, 2]), ([6, 7], [2, 3, 5]))


if __name__ == '__main__':
    unittest.main()
