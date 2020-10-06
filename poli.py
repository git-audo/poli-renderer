#!/usr/bin/python3.7

from tkinter import *
from models import cube
import camera, time, math
from geometry import Point2D, Point, Edge, Triangle, rotate

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


def rasterize():
    for t in triangles:
        triangleVertices = []
        triangleVertices.append(Point2D.getById(t.point1, vertices))
        triangleVertices.append(Point2D.getById(t.point2, vertices))
        triangleVertices.append(Point2D.getById(t.point3, vertices))

        top = Point2D('top', 0, -999)
        low1 = Point2D('low', 0, 999)
        low2 = Point2D('low', 0, 999)        
        for v in vertices2D:
            if v.id == t.point1 or v.id == t.point2 or v.id == t.point3:
                if v.y > top.y:
                    top = v
                elif v.y < low1.y and low1.y == 999:
                    low1 = v
                elif v.y < low2.y:
                    low2 = v


        half = Point2D('half', top.x, math.floor((low1.y + low2.y)/2))
        canvas.create_line(w-top.x, h+top.y, w-half.x, h+half.y, fill="#F6aa72", width=2.5)        

        
    
def drawEdges():
    for e in edges:
        p1 = Point2D.getById(e.point1, vertices2D)
        p2 = Point2D.getById(e.point2, vertices2D)
        canvas.create_line(w-p1.x, h+p1.y, w-p2.x, h+p2.y, fill="#F64C72", width=2.5)


def drawFrame():
    canvas.delete("all")
    computeVerticesTransformation()    
    drawEdges()
    rasterize()
    
        
def animateRotation():
    rotate(0.008, 0.002, vertices)
    drawFrame()
    canvas.after(20, animateRotation)


def loadModel():
    for id, x, y, z in cube.points:
        vertices.append(Point(id, x, y, z))

    for a, b, c in cube.triangles:
        triangles.append(Triangle(a, b, c))
    


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

    loadModel()
    animateRotation()
        
    root.mainloop()
    
