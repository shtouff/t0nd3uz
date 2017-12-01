from unittest import TestCase

from t0nd3uz.mower import Mower, Cmd, Dir
from t0nd3uz.point import Point


class MowerTestCase(TestCase):
    def test_mower(self):
        Mower(ini_dir=Dir.NORTH, ini_pos=Point(1, 2), program=[Cmd.RIGHT, Cmd.LEFT])

    def test_mower_str(self):
        self.assertEqual(
            str(Mower(ini_dir=Dir.NORTH, ini_pos=Point(1, 2), program=[])),
            '1 2 N'
        )

    def test_mower_do_next_step(self):
        lawn = (Point(0, 0), Point(9, 9))
        mower = Mower(ini_dir=Dir.NORTH, ini_pos=Point(1, 2), program=[Cmd.RIGHT, Cmd.FWD])

        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(1, 2))
        self.assertEqual(mower.cur_dir, Dir.EAST)

        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(2, 2))
        self.assertEqual(mower.cur_dir, Dir.EAST)

    def test_mower_dont_go_out_of_lawn_by_north(self):
        lawn = (Point(0, 0), Point(0, 0))
        mower = Mower(ini_dir=Dir.NORTH, ini_pos=Point(0, 0), program=[Cmd.FWD, Cmd.LEFT])

        mower.do_next_step(lawn=lawn, others=[])
        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(0, 0))
        self.assertEqual(mower.cur_dir, Dir.WEST)

    def test_mower_dont_go_out_of_lawn_by_west(self):
        lawn = (Point(0, 0), Point(0, 0))
        mower = Mower(ini_dir=Dir.WEST, ini_pos=Point(0, 0), program=[Cmd.FWD, Cmd.LEFT])

        mower.do_next_step(lawn=lawn, others=[])
        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(0, 0))
        self.assertEqual(mower.cur_dir, Dir.SOUTH)

    def test_mower_dont_go_out_of_lawn_by_south(self):
        lawn = (Point(0, 0), Point(0, 0))
        mower = Mower(ini_dir=Dir.SOUTH, ini_pos=Point(0, 0), program=[Cmd.FWD, Cmd.LEFT])

        mower.do_next_step(lawn=lawn, others=[])
        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(0, 0))
        self.assertEqual(mower.cur_dir, Dir.EAST)

    def test_mower_dont_go_out_of_lawn_by_east(self):
        lawn = (Point(0, 0), Point(0, 0))
        mower = Mower(ini_dir=Dir.EAST, ini_pos=Point(0, 0), program=[Cmd.FWD, Cmd.LEFT])

        mower.do_next_step(lawn=lawn, others=[])
        mower.do_next_step(lawn=lawn, others=[])
        self.assertEqual(mower.cur_pos, Point(0, 0))
        self.assertEqual(mower.cur_dir, Dir.NORTH)

    def test_mower_collide_first_wins(self):
        lawn = (Point(0, 0), Point(2, 2))
        m1 = Mower(ini_dir=Dir.EAST, ini_pos=Point(0, 1), program=[Cmd.FWD])
        m2 = Mower(ini_dir=Dir.WEST, ini_pos=Point(2, 1), program=[Cmd.FWD])
        m3 = Mower(ini_dir=Dir.SOUTH, ini_pos=Point(1, 2), program=[Cmd.FWD])

        m1.do_next_step(lawn=lawn, others=[m2, m3])
        m2.do_next_step(lawn=lawn, others=[m1, m3])
        m3.do_next_step(lawn=lawn, others=[m1, m2])

        self.assertEqual(m1.cur_pos, Point(1, 1))
        self.assertEqual(m1.cur_dir, Dir.EAST)

        self.assertEqual(m2.cur_pos, Point(2, 1))
        self.assertEqual(m2.cur_dir, Dir.WEST)

        self.assertEqual(m3.cur_pos, Point(1, 2))
        self.assertEqual(m3.cur_dir, Dir.SOUTH)
