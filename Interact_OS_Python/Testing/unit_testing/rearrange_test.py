from rearrange import rearrange_name
import unittest
# The unittest module includes a number of classes and methods that let us easily create unit tests for our code


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        return self.assertEqual(rearrange_name(testcase), expected)

if __name__ == '__main__':
    unittest.main()