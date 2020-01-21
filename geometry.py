
class Point2D:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def getById(id, points):
        point = [ p for p in points if p.id == id ]
        return point[0]

    
class Point(Point2D):
    def __init__(self, id, a, b, c):
        Point2D.__init__(self, id, a, b)
        self.z = c
    
    def coordinates(self):
        print(self.x, self.y, self.z)
        
        
class Edge:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
