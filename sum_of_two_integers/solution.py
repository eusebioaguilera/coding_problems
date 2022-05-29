import unittest


def find_sum_of_two(input_list, val):
    """
        Create a hash for visited values (val - actual_val)
    """

    result = False

    visited = dict()

    for _, item in enumerate(input_list):
        if item in visited:
            result = True

        visited[val - item] = True

    return result


class TestFindSumOfTwo(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_sum_of_two([2, 1, 8, 4, 7, 3], 3), True)

    def test2(self):
        self.assertEqual(find_sum_of_two([2, 1, 8, 4, 7, 3], 7), True)

    def test3(self):
        self.assertEqual(find_sum_of_two([2, 1, 8, 4, 7, 3], 20), False)

    def test4(self):
        self.assertEqual(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 1), False)

    def test5(self):
        self.assertEqual(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 2), False)

    def test6(self):
        self.assertEqual(find_sum_of_two([5, 7, 1, 2, 8, 4, 3], 7), True)


if __name__ == '__main__':
    unittest.main()
