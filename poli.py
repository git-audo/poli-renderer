#!/usr/bin/python3.7

from tkinter import *
import cube, camera, time, math

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


def computeVerticesTransformation():
    vertices2D.clear()
    edges.clear()
    for t in triangles:
        triangleVertices = []
        triangleVertices.append(Point2D.getById(t.point1, vertices))
        triangleVertices.append(Point2D.getById(t.point2, vertices))
        triangleVertices.append(Point2D.getById(t.point3, vertices))
        
        for v in triangleVertices:
            x = (camera.x - v.x)/((-camera.z + v.z + 100) * 0.001)
            y = (camera.y - v.y)/((-camera.z + v.z + 100) * 0.001)
            p = Point2D(v.id, x, y)
            vertices2D.append(p)
            # canvas.create_oval(w-x, h+y, w-x, h+y, width=4, outline="#F64C72")                    

        edges.append(Edge(t.point1, t.point2))
        edges.append(Edge(t.point1, t.point3))
        edges.append(Edge(t.point2, t.point3))


def drawEdges():
    for e in edges:
        p1 = Point2D.getById(e.point1, vertices2D)
        p2 = Point2D.getById(e.point2, vertices2D)
        canvas.create_line(w-p1.x, h+p1.y, w-p2.x, h+p2.y, fill="#F64C72")


def drawTop():
    # draw origin and camera
    canvas.create_oval(w, h, w, h, width=5, outline="#F64C72")
    canvas.create_oval(w+camX, h+camZ , w+camX, h+camZ, width=10, outline="white")
    canvas.create_line(0, 0, 0, 500, fill="green") 

    for v in vertices:
        canvas.create_oval(w+v.x, h+v.z, w+v.x, h+v.z, width=5, outline="#F64C72")
    for e in edges:
        id1 = e.point1
        id2 = e.point2
        p1 = Point2D.getById(id1, vertices)
        p2 = Point2D.getById(id2, vertices)
        canvas.create_line(w+p1.x, h+p1.y, w+p2.x, h+p2.y, fill="#F64C72")


def rotate():
    modelRotateY = 0.008
    modelRotateX = 0.002    
    for v in vertices:
        x = v.x
        y = v.y
        
        v.x = math.cos(modelRotateY)*v.x + math.sin(modelRotateY)*v.z 
        v.z = -math.sin(modelRotateY)*x + math.cos(modelRotateY)*v.z

        v.y = math.cos(modelRotateX)*v.y + math.sin(modelRotateX)*v.z
        v.z = -math.sin(modelRotateX)*y + math.cos(modelRotateX)*v.z


def animateRotation():
    rotate()
    canvas.delete("all")
    computeVerticesTransformation()
    drawEdges()
    canvas.after(20, animateRotation)


if __name__ == '__main__':
    root = Tk()
    w = root.winfo_screenwidth()/2
    h = root.winfo_screenheight()/2
    root.wm_attributes("-type", "splash")
    canvas = Canvas(root, width=1200, height=600, bg="#282828")
    canvas.pack()

    camX = 80 ; camY = -50 ; camZ = -130
    camera = camera.Camera(camX, camY, camZ)

    origin = Point(0, 0, 0, 0)
    xVersor = Point(97, 10, 0, 0)
    yVersor = Point(98, 0, 10, 0)
    zVersor = Point(99, 0, 0, 10)
    ox = Edge(origin.id, xVersor.id)
    oy = Edge(origin.id, yVersor.id)
    oz = Edge(origin.id, zVersor.id)
    
    vertices = [ origin ]
    vertices2D = []
    triangles = []    
    edges = []

    for id, x, y, z in cube.points:
        vertices.append(Point(id, x, y, z))

    for a, b, c in cube.triangles:
        triangles.append(Triangle(a, b, c))

    animateRotation()
        
    root.mainloop()
    
