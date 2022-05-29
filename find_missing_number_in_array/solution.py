import unittest


def find_missing(input):
    """
        Compute the sum of the values of the input and the expected sum of the first N numbers
        The diff is the missing value
    """
    input_sum = sum(input)
    expected_sum = sum(list(range(max(input) + 1)))
    diff = expected_sum - input_sum
    return diff


class TestFindMissing(unittest.TestCase):
    def testFindMissingNumber(self):
        val = find_missing([3, 7, 1, 2, 8, 4, 5])
        self.assertEqual(val, 6)


if __name__ == '__main__':
    unittest.main()
