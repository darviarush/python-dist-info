import sys
import unittest

sys.path.append(".")

from dist_info import files, modules

class DistInfoTestCase(unittest.TestCase):

    def test_dist_info(self):
        """ тест функций """

        self.assertEqual(123, 123, '')


if __name__ == '__main__':
    unittest.main()

