import unittest

class CheckVolume(unittest.TestCase):
    def test_volume_cube(self):
        x = 5.555
        result = test_volume_cube(x)
        self.assertAlmostEqual(result, x*x*x)