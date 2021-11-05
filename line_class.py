import numpy as np
import math

from point_class import Point
from check_error import is_equal

class Line():
    """equation of a line in Descartes Oxy has a form :
        ax + by + c = 0, it's direction vector is (a, b)
        with a, b, c are real numbers.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def is_line(self):
        if is_equal(self.a**2 + self.b**2, 0):
            return False
        else: 
            return True

    def __repr__(self): 
        if self.is_line() == False:
            mess_noti = "\nNot exist a line has equation: %s*x + %s*y + %s = 0" % (self.a, self.b, self.c)
        else: 
            mess_noti = "\nEquation of the line is %s*x + %s*y + %s = 0" % (self.a, self.b, self.c)
        return mess_noti
    
    def num_intersect(self, an_other_line):
        if (self.is_line() and an_other_line.is_line()) == False:
            return False
        else:
            a1, b1, c1 = self.a, self.b, self.c 
            a2, b2, c2 = an_other_line.a, an_other_line.b, an_other_line.c
            # if a1*b2 == a2*b1:
            if is_equal(a1*b2, a2*b1):
                if c1 != c2: # two lines are parallel
                    intersections = 0
                else: # two lines are coincident
                    intersections = math.inf
            else:
                intersections = 1
            return intersections
    
    def get_two_line_intersection(self, an_other_line):
        num_intersect = self.num_intersect(an_other_line)
        if num_intersect == 0:
            return print("Two lines are parallel and have no intersection")
        elif num_intersect == math.inf:
            return print("Two lines are coincident")
        else :
            """
            Solve the system of equations:
            a_1*x + b_1*y = -c_1
            a_2*x + b_2*y = -c_2
            or solve equation [a1 b1, a2 b2]*[x,y] = [-c1, -c2]
            """
            a1, b1, c1 = self.a, self.b, self.c 
            a2, b2, c2 = an_other_line.a, an_other_line.b, an_other_line.c
            sys_eqs_mat = np.array([[a1, b1], [a2, b2]])
            sys_eqs_value = np.array([-c1, -c2])
            solutions = np.linalg.solve(sys_eqs_mat, sys_eqs_value)
            
            intersections = Point(solutions[0], solutions[1])
            return intersections
    
    def get_distance_from_point_to_line(point, self):
        """
        this method calculate distance from a point to a line
        a point: Point(x0, y0)
        a line: a*x + b*y + c = 0
        ==> dist(line, point) = abs(a*x0 + b*y0 + c)/sqrt(a**2 + b**2)
        """
        x0, y0 = point.x, point.y
        distance = abs(self.a*x0 + self.b*y0 + self.c)/math.sqrt(self.a**2 + self.b**2)
        return distance
    
    def get_line(point1, point2):
        x1, y1 = point1.x, point1.y
        x2, y2 = point2.x, point2.y
        # if x1 == x2 and y1 == y2:
        if is_equal(x1, x2) == True and is_equal(y1, y2) == True:
            return print("Have infinitive lines throw this two lines!")
        else: 
            # line's direction_vector = (x2 - x1, y2 - y1)
            # line's normal vector = (y1 - y2, x2 - x1)
            # line's equation: ax + by + c = 0 or (y1 - y2)*x + (x2 - x1)*y + (x1*y2 - x2*y1) = 0
            line_a = y1 - y2
            line_b = x2 - x1
            line_c = (x1*y2 - x2*y1)
            return Line(line_a, line_b, line_c)
    
    def is_point_on_line(point, self):
        x_point = point.x
        y_point = point.y
        check_point_in_line = self.a*x_point + self.b*y_point + self.c
        if is_equal(check_point_in_line, 0):
            return True
        else:
            return False
