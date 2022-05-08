from rearrange import rearrange_name
import unittest
# The unittest module includes a number of classes and methods that let us easily create unit tests for our code


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        return self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        return self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        return self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        return self.assertEqual(rearrange_name(testcase), expected)


if __name__ == '__main__':
    unittest.main()


"""
        Edge Cases
        Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of 
        the ranges of input we imagine our programs will typically work with. Edge cases usually need special 
        handling in scripts in order for the code to continue to behave correctly. 
        
         Other kinds of edge cases usually include things like passing zero to a function that expects a number, 
         or negative numbers, or extremely large numbers. These types of conditions are good to consider when writing 
         your test, since they can cause your code to crash or behave in unexpected ways.
"""