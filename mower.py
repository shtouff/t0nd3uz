from enum import Enum

from point import Point


class Cmd(Enum):
    FWD = 'F'
    LEFT = 'L'
    RIGHT = 'R'


class Dir(Enum):
    NORTH = 'N'
    WEST = 'W'
    SOUTH = 'S'
    EAST = 'E'


LeftRot = {
    Dir.NORTH: Dir.WEST,
    Dir.WEST: Dir.SOUTH,
    Dir.SOUTH: Dir.EAST,
    Dir.EAST: Dir.NORTH,
}
RightRot = {
    Dir.NORTH: Dir.EAST,
    Dir.EAST: Dir.SOUTH,
    Dir.SOUTH: Dir.WEST,
    Dir.WEST: Dir.NORTH,
}
FwdMove = {
    Dir.NORTH: lambda p: Point(p.x, p.y + 1),
    Dir.WEST: lambda p: Point(p.x - 1, p.y),
    Dir.SOUTH: lambda p: Point(p.x, p.y - 1),
    Dir.EAST: lambda p: Point(p.x + 1, p.y),
}


class Mower:
    def __init__(self, ini_dir, ini_pos, program):
        self.__cur_dir = ini_dir
        self.__cur_pos = ini_pos
        self.__program = program
        self.__cur_step = 0

    @property
    def cur_dir(self):
        return self.__cur_dir

    @property
    def cur_pos(self):
        return self.__cur_pos

    @property
    def program(self):
        return self.__program

    def do_next_step(self, lawn, others):
        if self.__cur_step >= len(self.__program):
            return

        cur_cmd = Cmd(self.__program[self.__cur_step])
        if cur_cmd is Cmd.LEFT:
            self.__cur_dir = LeftRot[self.__cur_dir]
        elif cur_cmd is Cmd.RIGHT:
            self.__cur_dir = RightRot[self.__cur_dir]
        elif self._can_move_fwd(lawn, others):
            self.__cur_pos = FwdMove[self.__cur_dir](self.__cur_pos)
        self.__cur_step += 1

    def _can_move_fwd(self, lawn, others):
        if self.__cur_dir is Dir.NORTH and self.__cur_pos.y == lawn[1].y or \
                self.__cur_dir is Dir.WEST and self.__cur_pos.x == lawn[0].x or \
                self.__cur_dir is Dir.SOUTH and self.__cur_pos.y == lawn[0].y or \
                self.__cur_dir is Dir.EAST and self.__cur_pos.x == lawn[1].x:
            return False

        for mower in others:
            if mower.cur_pos == FwdMove[self.__cur_dir](self.__cur_pos):
                return False

        return True

    def __str__(self):
        return '{} {} {}'.format(self.__cur_pos.x, self.__cur_pos.y, self.__cur_dir.value)
