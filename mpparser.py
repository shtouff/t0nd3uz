import io
import re

from point import Point
from mower import Mower, Cmd, Dir

LAWN_REGEX = re.compile(r'^(?P<x>[0-9]+) (?P<y>[0-9]+)\n$')
MOWER_INIT_REGEX = re.compile(r'^(?P<x>[0-9]+) (?P<y>[0-9]+) (?P<dir>[NSWE]+)\n$')
MOWER_PROGRAM_REGEX = re.compile(r'^(?P<prog>[FRL]+)\n$')


class MowerProgramParseError(BaseException):
    pass


class MowerProgramParser:
    def __init__(self, stream: io.TextIOBase):
        self.__mowers = []
        stream.seek(0, io.SEEK_SET)
        cmdlines = stream.readlines()

        m = LAWN_REGEX.match(cmdlines[0])
        if m is None:
            raise MowerProgramParseError('could not parse lawn upper right coords')
        self.__lawn = (Point(0, 0), Point(int(m.group('x')), int(m.group('y'))))

        cmdlen = len(cmdlines) - 1
        if cmdlen % 2 != 0:
            raise MowerProgramParseError('odd number of mower lines')

        for i in range(int(cmdlen / 2)):
            mi = MOWER_INIT_REGEX.match(cmdlines[i * 2 + 1])
            if mi is None:
                raise MowerProgramParseError('could not parse initial position/direction for mower #{}'.format(i))

            mp = MOWER_PROGRAM_REGEX.match(cmdlines[i * 2 + 2])
            if mp is None:
                raise MowerProgramParseError('could not parse program for mower #{}'.format(i))

            ini_pos = Point(int(mi.group('x')), int(mi.group('y')))
            if ini_pos >= self.__lawn[1] and ini_pos != self.__lawn[1]:
                raise MowerProgramParseError('initial position for mower #{} can\'t be out of the lawn'.format(i))

            self.__mowers.append(Mower(
                ini_pos=ini_pos,
                ini_dir=Dir(mi.group('dir')),
                program=[Cmd(x) for x in mp.group('prog')],
            ))

    @property
    def lawn(self):
        """
        :return: a tuple of two Point objects: the bottom left and the upper right of the lawn.
        """
        return self.__lawn

    @property
    def mowers(self):
        """
        :return: a list of Mower objects.
        """
        return self.__mowers
