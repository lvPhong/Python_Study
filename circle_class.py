from point_class import Point
from line_class import Line
from check_error import is_equal

import matplotlib.pyplot as plt
import math
PI = math.pi
# shoud be use math.pi


class Circle():

    def __init__(self, center, radius):
        self.center = center  # center point
        self.radius = radius

    def __repr__(self):
        return "Circle has center %s and radius equals %s" % (self.center, self.radius)

    @property
    def perimeter(self):
        return 2*PI*self.radius

    @property
    def area(self):
        return PI*self.radius**2

    # line vs circle:
    def line_intersect_circle(self, line):
        """
        This method return the number of intersections of the line with the circle.
        """
        center = self.center
        dist_center_to_line = Line.get_distance_from_point_to_line(
            center, line)
        if dist_center_to_line > self.radius:
            intersections = 0
        elif dist_center_to_line < self.radius:
            intersections = 2
        else:
            intersections = 1
        return intersections

    # circle vs circle
    def is_coincidence_circles(self, an_other_circle):
        c1, c2 = self.center, an_other_circle.center
        r1, r2 = self.radius, an_other_circle.radius
        # should be use math.isclose()
        if Point.is_coincide_points(c1, c2) == True and is_equal(r1, r2) == True:
            return True
        else:
            return False

    def circle_intersect_circle(self, an_other_circle):
        """
        This method return the number of intersections of two circles.
        Circle(C1, r1) vs Circle(C2, r2)
            if r1 == r2, and C1 == C2, intersections = inf
        d is distance from C1, C2(two centers of the two Circles)
            if r1 + r2 > d > |r1 - r2| --> intersections = 2
            if r1 + r2 = d or d = r1 or d = r2 --> intersections = 1
            other cases --> intersections = 0 
        """
        r1, r2 = self.radius, an_other_circle.radius
        center1, center2 = self.center, an_other_circle.center
        distance_between_two_centers = Point.distance(center1, center2)
        r_sum = r1 + r2
        r_sub = abs(r1 - r2)
        d = distance_between_two_centers
        intersections = 0
        if Circle.is_coincidence_circles(self, an_other_circle) == True:
            intersections = math.inf
        if r_sub < d and d < r_sum:
            intersections = 2
        if d in [r_sum, r_sub]:
            intersections = 1
        return intersections
