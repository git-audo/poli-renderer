#!/usr/bin/python3.7

from tkinter import *
from models import cube
from models.cube import n_triangles
import camera, time, math
from geometry import Point2D, Point, Edge, Triangle, rotate, translate
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
        return True
    else:
        return False

    
def rasterize(v, c, res):
    colors = [
        "#f6aa72",
        "#ffaaff",
        "#aaaaaa",
    ]
    
    for i in range(-100, 900, res):
        for j in range(-500, 50, res):  
            if (edgeFunction(v[0][0], v[0][1], v[1][0], v[1][1], i, j) and
                edgeFunction(v[2][0], v[2][1], v[0][0], v[0][1], i, j) and
                edgeFunction(v[1][0], v[1][1], v[2][0], v[2][1], i, j)):
                canvas.create_oval(w/2+i, h/2+j, w/2+i, h/2+j, width=4, outline=colors[c%3])
        

def drawLine(x1, y1, x2, y2):
        canvas.create_line(w/2+x1, h/2+y1, w/2+x2, h/2+y2, fill="#F64C72", width=2.5)

        
def drawFrame():
    for i, t in enumerate(triangles):
        vertices2d.clear()
        # for each triangle vertex compute the trasformation from 3d space to 2d space
        for v in t:
            x = (camera.x - v[0])/((-camera.z + v[2] + 100) * 0.001)
            y = (camera.y - v[1])/((-camera.z + v[2] + 100) * 0.001)
            vertices2d.append((x, y))


        drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[1][0], vertices2d[1][1])
        drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[2][0], vertices2d[2][1])
        drawLine(vertices2d[1][0], vertices2d[1][1], vertices2d[2][0], vertices2d[2][1])
        rasterize(vertices2d, i, 10)

        
def animateRotation():
    canvas.delete("all")
    rotate(triangles)
    #translate(triangles, 0.02, 0.02, 0.0)
    drawFrame()
    canvas.after(20, animateRotation)


def loadModel():
    for t in n_triangles:
        triangles.append(t)
        

if __name__ == '__main__':
    root = Tk()
    w = root.winfo_screenwidth()/1.5
    h = root.winfo_screenheight()/1.5
    root.wm_attributes("-type", "splash")
    canvas = Canvas(root, width=w, height=h, bg="#282828")
    canvas.pack()

    camX = 0 ; camY = 0 ; camZ = -10
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
    
