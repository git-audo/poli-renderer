#!/usr/bin/python3.7

from tkinter import *
from models import cube
from models.cube import n_triangles
import camera, time, math
from geometry import Point2D, Point, Edge, Triangle, rotate
from numpy import arange


# unused
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


        
def edgeFunction(x1, y1, x2, y2, p1, p2):
    cond = ((p1-x1)*(y2-y1)-(p2-y1)*(x2-x1))
    if cond > 0:
        return False
    else:
        return True

    
def rasterize(v):
    for i in range(0, math.floor(w), 30):
            for j in range(0, math.floor(h), 30):
                if edgeFunction(v[0][0], v[0][1], v[1][0], v[1][1], i, j)
                  and edgeFunction(v[0][0], v[0][1], v[2][0], v[2][1], i, j)
                    canvas.create_oval(i, j, i, j, width=4, outline="#F64C72")                         

    
        # top = Point2D('top', 0, -999)
        # low = Point2D('low', 0, 999)
        # mid = Point2D('low', 0, 999)        
        # for v in vertices:
        #     if v.id == t.point1 or v.id == t.point2 or v.id == t.point3:
        #         if v.y > top.y:
        #             top = v
        #         elif v.y < low.y:
        #             if low.y != 999:
        #                 mid = low
        #                 low = v
        #         else:
        #             mid = v


        # half = Point2D('half', top.x, math.floor((low.y + mid.y)/2))
        # canvas.create_line(w-top.x, h+top.y, w-half.x, h+half.y, fill="#F6aa72", width=2.5)        

        # print(top.y, mid.y)
        # for i in arange(top.y, low.y, 0.1):
        #     canvas.create_line(w-top.x-100, h+top.y+i, w-top.x+100, h+top.y+i, fill="#F6aa72", width=2.5)        
        

def drawLine(x1, y1, x2, y2):
        canvas.create_line(w-x1, h+y1, w-x2, h+y2, fill="#F64C72", width=2.5)

        
def drawFrame():
    for t in n_triangles:
        vertices2d.clear()
        # for each triangle vertex compute the trasformation from 3d space to 2d space
        for v in t:
            x = (camera.x - v[0])/((-camera.z + v[2] + 100) * 0.001)
            y = (camera.y - v[1])/((-camera.z + v[2] + 100) * 0.001)
            vertices2d.append((x, y))


        drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[1][0], vertices2d[1][1])
        drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[2][0], vertices2d[2][1])
        drawLine(vertices2d[1][0], vertices2d[1][1], vertices2d[2][0], vertices2d[2][1])

        rasterize(vertices2d)

        
def animateRotation():
    canvas.delete("all")
    rotate(triangles)
    drawFrame()
    canvas.after(20, animateRotation)


def loadModel():
    for t in n_triangles:
        triangles.append(t)
        

if __name__ == '__main__':
    root = Tk()
    w = root.winfo_screenwidth()/2
    h = root.winfo_screenheight()/2
    root.wm_attributes("-type", "splash")
    canvas = Canvas(root, width=1200, height=600, bg="#282828")
    canvas.pack()

    camX = 60 ; camY = 10 ; camZ = 5
    camera = camera.Camera(camX, camY, camZ)

    #vertices = [ origin ]
    vertices2D = []
    triangles = []
    edges = []

    vertices3d = [] # not used for now
    vertices2d = []

    loadModel()
    animateRotation()
        
    root.mainloop()
    
