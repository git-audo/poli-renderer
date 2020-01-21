#!/usr/bin/python3.7

from tkinter import *
from models import cube
import camera, geometry, time, math
from geometry import Point2D, Point, Edge, Triangle

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
        canvas.create_line(w-p1.x, h+p1.y, w-p2.x, h+p2.y, fill="#F64C72", width=2.5)


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

    camX = 90 ; camY = -50 ; camZ = -130
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
    
