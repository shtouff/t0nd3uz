from unittest import TestCase

from t0nd3uz.point import Point


class PointTestCase(TestCase):
    def test_point_without_coords(self):
        with self.assertRaises(TypeError):
            Point()

    def test_point_with_int_coords(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

    def test_point_with_non_int_coords(self):
        with self.assertRaises(TypeError):
            Point(0.1, 0)
        with self.assertRaises(TypeError):
            Point('2', 0)

    def test_point_with_negative_coords(self):
        with self.assertRaises(ValueError):
            Point(-1, 0)

    def test_equal(self):
        self.assertEqual(Point(1, 2), Point(1, 2))

    def test_not_equal(self):
        self.assertNotEqual(Point(1, 2), Point(2, 1))

    def test_gt(self):
        self.assertGreater(Point(3, 3), Point(2, 2))
        self.assertGreater(Point(3, 2), Point(2, 2))
        self.assertGreater(Point(2, 3), Point(2, 2))
        with self.assertRaises(AssertionError):
            self.assertGreater(Point(2, 2), Point(2, 2))

    def test_ge(self):
        self.assertGreaterEqual(Point(3, 3), Point(2, 2))
        self.assertGreaterEqual(Point(3, 2), Point(2, 2))
        self.assertGreaterEqual(Point(2, 3), Point(2, 2))
        self.assertGreaterEqual(Point(2, 2), Point(2, 2))

    def test_lt(self):
        self.assertLess(Point(1, 1), Point(2, 2))
        with self.assertRaises(AssertionError):
            self.assertLess(Point(1, 2), Point(2, 2))
        with self.assertRaises(AssertionError):
            self.assertLess(Point(2, 1), Point(2, 2))
        with self.assertRaises(AssertionError):
            self.assertLess(Point(2, 2), Point(2, 2))

    def test_le(self):
        self.assertLessEqual(Point(1, 1), Point(2, 2))
        self.assertLessEqual(Point(1, 2), Point(2, 2))
        self.assertLessEqual(Point(2, 1), Point(2, 2))
        self.assertLessEqual(Point(2, 2), Point(2, 2))
