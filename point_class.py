from check_error import is_equal
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self): 
        return "Point(%s, %s)" % (self.x, self.y)
    
    def is_coincide_points(self, an_other_point):
        if is_equal(self.x, an_other_point.x) == True and is_equal(self.y, an_other_point.y) == True:
            return True
        else: 
            return False
    
    def distance(self, an_other_point, metric = "L2"):
        """
        metric in this method is used to calculate the distance
        of two points by using normal in Euclid
        "L1" or "L1", etc
        """
        normal_metric = int(metric[1]) # 2 in "L2"
        dx = self.x - an_other_point.x
        dy = self.y - an_other_point.y
        distance_ = (abs(dx)**normal_metric + abs(dy)**normal_metric)**(1/normal_metric)    
        return distance_