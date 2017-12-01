import io
from unittest import TestCase

from mower import Dir
from mpparser import MowerProgramParser, MowerProgramParseError
from point import Point


p1 = """3 3
1 1 N
FF
"""

p2 = """5 5
1 2 N
LFLFLFLFF
3 3 E
FFRFFRFRRF
"""

p3 = """0 0 5 5
"""

p4 = """5 5
1 2 N
LFLFLF
3 3 E
"""

p5 = """10 10
1 2 X
LF
"""

p6 = """42 43
1 2 N
FXXXXF
"""

p7 = """2 2
3 2 N
FF
"""

p8 = """2 2
1 1 N
FF
1 1 E
FF
"""

class MowerTestCase(TestCase):
    def test_parser_p1(self):
        parser = MowerProgramParser(stream=io.StringIO(p1))
        self.assertEqual(parser.lawn, (Point(0, 0), Point(3, 3)))
        self.assertEqual(len(parser.mowers), 1)
        self.assertEqual(parser.mowers[0].cur_dir, Dir.NORTH)
        self.assertEqual(parser.mowers[0].cur_pos, Point(1, 1))

    def test_parser_p2(self):
        parser = MowerProgramParser(stream=io.StringIO(p2))
        self.assertEqual(parser.lawn, (Point(0, 0), Point(5, 5)))
        self.assertEqual(len(parser.mowers), 2)

        self.assertEqual(parser.mowers[0].cur_dir, Dir.NORTH)
        self.assertEqual(parser.mowers[0].cur_pos, Point(1, 2))

        self.assertEqual(parser.mowers[1].cur_dir, Dir.EAST)
        self.assertEqual(parser.mowers[1].cur_pos, Point(3, 3))

    def test_parser_p3(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p3))

        self.assertEqual(str(cm.exception), 'could not parse lawn upper right coords')

    def test_parser_p4(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p4))

        self.assertEqual(str(cm.exception), 'odd number of mower lines')

    def test_parser_p5(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p5))

        self.assertEqual(str(cm.exception), 'could not parse initial position/direction for mower #0')

    def test_parser_p6(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p6))

        self.assertEqual(str(cm.exception), 'could not parse program for mower #0')

    def test_parser_p7(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p7))

        self.assertEqual(str(cm.exception), 'initial position for mower #0 can\'t be out of the lawn')

    def test_parser_p8(self):
        with self.assertRaises(MowerProgramParseError) as cm:
            MowerProgramParser(stream=io.StringIO(p8))

        self.assertEqual(str(cm.exception), 'initial position for mower #1 collides with another mower')
