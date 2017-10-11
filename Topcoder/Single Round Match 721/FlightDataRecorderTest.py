import unittest
import math
from FlightDataRecorder import FlightDataRecorder


class FlightDataRecorderTest(unittest.TestCase):

    def assertTcFloatEqual(self, expected, received, msg=None):
        eps = 1e-9
        if math.isnan(received) or math.isnan(expected) \
           or abs(received - expected) > eps * max(1.0, abs(expected)):
            msg = self._formatMessage(msg, "%s != %s" % (expected, received))
            raise self.failureException(msg)

    def test_Example0(self):
        heading = [
            90,
            0
        ]
        distance = [
            3,
            4
        ]
        __expected = 5.0
        __result = FlightDataRecorder().getDistance(heading, distance)
        self.assertTcFloatEqual(__expected, __result)

    def test_Example1(self):
        heading = [
            37,
            37,
            37,
            37
        ]
        distance = [
            1,
            10,
            100,
            1000
        ]
        __expected = 1111.0
        __result = FlightDataRecorder().getDistance(heading, distance)
        self.assertTcFloatEqual(__expected, __result)

    def test_Example2(self):
        heading = [
            0,
            120,
            240,
            0,
            120,
            240
        ]
        distance = [
            999,
            999,
            999,
            999,
            999,
            999
        ]
        __expected = 6.431098710768743E-13
        __result = FlightDataRecorder().getDistance(heading, distance)
        self.assertTcFloatEqual(__expected, __result)

    def test_Example3(self):
        heading = [
            76,
            321,
            214,
            132,
            0,
            359,
            74,
            65,
            213
        ]
        distance = [
            621,
            235,
            698,
            1,
            35,
            658,
            154,
            426,
            965
        ]
        __expected = 153.54881555325184
        __result = FlightDataRecorder().getDistance(heading, distance)
        self.assertTcFloatEqual(__expected, __result)

    def test_Example4(self):
        heading = [
            0
        ]
        distance = [
            1
        ]
        __expected = 1.0
        __result = FlightDataRecorder().getDistance(heading, distance)
        self.assertTcFloatEqual(__expected, __result)


if __name__ == '__main__':
    unittest.main()
