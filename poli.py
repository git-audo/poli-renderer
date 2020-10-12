#!/usr/bin/python3.7

from tkinter import *
from models import cube
from models.cube import n_triangles
import camera, time, math
from geometry import Triangle, rotate, translate
from numpy import arange


def edgeFunction(x1, y1, x2, y2, p1, p2):
    cond = ((p1-x1)*(y2-y1)-(p2-y1)*(x2-x1))
    if cond > 0:
        return True
    else:
        return False

    
def rasterize(v, c, res):
    colors = [
        "#e42256",
        "#ff8370",
        "#00b1b0",
        "#fec84d",        
    ]
    
    for i in range(-500, 200, res):
        for j in range(-300, 300, res):  
            if (edgeFunction(v[0][0], v[0][1], v[1][0], v[1][1], i, j) and
                edgeFunction(v[2][0], v[2][1], v[0][0], v[0][1], i, j) and
                edgeFunction(v[1][0], v[1][1], v[2][0], v[2][1], i, j)):
                canvas.create_oval(w/2+i, h/2+j, w/2+i, h/2+j, width=6, outline=colors[c%4])
        

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

        if wireframeOn:
            drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[1][0], vertices2d[1][1])
            drawLine(vertices2d[0][0], vertices2d[0][1], vertices2d[2][0], vertices2d[2][1])
            drawLine(vertices2d[1][0], vertices2d[1][1], vertices2d[2][0], vertices2d[2][1])

        rasterize(vertices2d, i, 8)

        
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
    canvas = Canvas(root, width=w, height=h, bg="#ffffff")
    canvas.pack()

    camX = 3 ; camY = 5 ; camZ = 65
    camera = camera.Camera(camX, camY, camZ)

    wireframeOn = False
    
    #vertices = [ origin ]
    vertices2D = []
    triangles = []
    edges = []

    vertices3d = [] # not used for now
    vertices2d = []

    loadModel()
    animateRotation()

    root.mainloop()
    
