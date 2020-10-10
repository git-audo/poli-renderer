import math

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


def translate(dx, dy, dz):
    for t in triangles:
        for v in t:
            v[0] = v[0] + dx
            v[1] = v[1] + dy
            v[2] = v[2] + dz
        

def rotate(triangles):
    modelRotateY = 0.020
    modelRotateX = 0.020
    for t in triangles:
        for v in t:
            x = v[0]
            y = v[1]
            z = v[2]
            
            v[0] = math.cos(modelRotateY)*x + math.sin(modelRotateY)*z
            v[2] = -math.sin(modelRotateY)*x + math.cos(modelRotateY)*z
            
            v[1] = math.cos(modelRotateX)*y + math.sin(modelRotateX)*v[2]
            v[2] = -math.sin(modelRotateX)*y + math.cos(modelRotateX)*v[2]

            
