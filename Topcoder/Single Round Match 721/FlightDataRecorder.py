import math


class FlightDataRecorder:

    class Plane:
        def __init__(self):
            self.x = 0
            self.y = 0

    def getDistance(self, heading, distance):
        plane = self.Plane()
        for h, d in zip(heading, distance):
            radians = math.radians(h)
            sin = math.sin(radians)
            cos = math.cos(radians)

            plane.x += sin * d
            plane.y += cos * d

        return (plane.x ** 2 + plane.y ** 2) ** 0.5
