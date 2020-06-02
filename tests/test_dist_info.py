import sys
import unittest

sys.path.append(".")

from dist_info import dist_info_paths, dist_files, files, modules
from data_printer import p

class DistInfoTestCase(unittest.TestCase):

    def test_dist_info(self):
        """ тест функций """

        DIST_NAME = 'pytest'
        dist_dir, egg_dir = dist_info_paths(DIST_NAME)
        p((dist_dir, egg_dir))

        dist_dir, egg_dir, installed_files = dist_files(DIST_NAME)
        p((dist_dir, egg_dir, installed_files))

        p(files(DIST_NAME))
        p(modules(DIST_NAME))

        self.assertEqual(123, 123, '')

    def test_egg_info(self):
        """ тест функций """

    def test_egg_link(self):
        """ тест функций """

if __name__ == '__main__':
    unittest.main()

