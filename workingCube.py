
#Made by Trevor Dolbow
#9/27/2020
import tkinter
import time
import math
from random import seed
from random import random


"""Canvas Size Val"""
xSize = 500
ySize = 500
xOffset = 0
seed(time)
class cube:
    point1 = [-100,100,100]
    point2 = [100,100,100]
    point3 = [100,-100,100]
    point4 = [-100,-100,100]
    point5 = [-100,100,-100]
    point6 = [100,100,-100]
    point7 = [100,-100,-100]
    point8 = [-100,-100,-100]
   

        
    def getFrontSide(self):
        return [self.point1[0],self.point1[1],self.point2[0],self.point2[1],self.point3[0],self.point3[1],self.point4[0],self.point4[1],self.point1[0],self.point1[1]]
    
    def getTopSide(self):
        return [self.point1[0],self.point1[1],self.point5[0],self.point5[1],self.point6[0],self.point6[1],self.point2[0],self.point2[1],self.point1[0],self.point1[1]]
    def getLeftSide(self):
        return [self.point1[0],self.point1[1],self.point5[0],self.point5[1],self.point8[0],self.point8[1],self.point4[0],self.point4[1],self.point1[0],self.point1[1]]
    def getRightSide(self):
        return [self.point2[0],self.point2[1],self.point6[0],self.point6[1],self.point7[0],self.point7[1],self.point3[0],self.point3[1],self.point2[0],self.point2[1]]
    def getBottomSide(self):
        return [self.point4[0],self.point4[1],self.point8[0],self.point8[1],self.point7[0],self.point7[1],self.point3[0],self.point3[1],self.point4[0],self.point4[1]]
    def getBackSide(self):
        return [self.point5[0],self.point5[1],self.point6[0],self.point6[1],self.point7[0],self.point7[1],self.point8[0],self.point8[1],self.point5[0],self.point5[1]]
    def colorOrder(self):
        frontSideAvg =  (self.point1[2]+self.point2[2]+self.point3[2]+self.point4[2])/4
        topSideAvg =  (self.point1[2]+self.point5[2]+self.point6[2]+self.point2[2])/4
        bottomSideAvg =  (self.point4[2]+self.point8[2]+self.point7[2]+self.point3[2])/4
        leftSideAvg =  (self.point1[2]+self.point5[2]+self.point8[2]+self.point4[2])/4
        rightSideAvg =  (self.point2[2]+self.point6[2]+self.point7[2]+self.point3[2])/4
        backSideAvg =  (self.point5[2]+self.point6[2]+self.point7[2]+self.point8[2])/4
        order = [frontSideAvg,topSideAvg,bottomSideAvg,leftSideAvg,rightSideAvg,backSideAvg]
        order.sort(reverse=True)

        return order
    def getFrontSideZAvg(self):
        frontSideAvg =  (self.point1[2]+self.point2[2]+self.point3[2]+self.point4[2])/4
        return frontSideAvg
    def getTopSideZAvg(self):
        topSideAvg =  (self.point1[2]+self.point5[2]+self.point6[2]+self.point2[2])/4
        return topSideAvg
    def getLeftSideZAvg(self):
        leftSideAvg =  (self.point1[2]+self.point5[2]+self.point8[2]+self.point4[2])/4
        return leftSideAvg
    def getRightSideZAvg(self):
        rightSideAvg =  (self.point2[2]+self.point6[2]+self.point7[2]+self.point3[2])/4
        return rightSideAvg
    def getBottomSideZAvg(self):
        bottomSideAvg =  (self.point4[2]+self.point8[2]+self.point7[2]+self.point3[2])/4
        return bottomSideAvg
    def getBackSideZAvg(self):
        backSideAvg =  (self.point5[2]+self.point6[2]+self.point7[2]+self.point8[2])/4
        return backSideAvg
    
        
        
    
    
    def rotateZ(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        x = self.point1[0]
        y = self.point1[1]
        self.point1[0] = x*cosTheta -y*sinTheta 
        self.point1[1] = y*cosTheta + x*sinTheta
        
        x = self.point2[0]
        y = self.point2[1]
        self.point2[0] = x*cosTheta -y*sinTheta 
        self.point2[1] = y*cosTheta + x*sinTheta
        
        x = self.point3[0]
        y = self.point3[1]
        self.point3[0] = x*cosTheta -y*sinTheta 
        self.point3[1] = y*cosTheta + x*sinTheta
        
        x = self.point4[0]
        y = self.point4[1]
        self.point4[0] = x*cosTheta -y*sinTheta 
        self.point4[1] = y*cosTheta + x*sinTheta
        
        x = self.point5[0]
        y = self.point5[1]
        self.point5[0] = x*cosTheta -y*sinTheta 
        self.point5[1] = y*cosTheta + x*sinTheta
        
        x = self.point6[0]
        y = self.point6[1]
        self.point6[0] = x*cosTheta -y*sinTheta 
        self.point6[1] = y*cosTheta + x*sinTheta
        
        x = self.point7[0]
        y = self.point7[1]
        self.point7[0] = x*cosTheta -y*sinTheta 
        self.point7[1] = y*cosTheta + x*sinTheta
        
        x = self.point8[0]
        y = self.point8[1]
        self.point8[0] = x*cosTheta -y*sinTheta 
        self.point8[1] = y*cosTheta + x*sinTheta
    
    def rotateX(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        x = self.point1[1]
        y = self.point1[2]
        self.point1[1] = x*cosTheta -y*sinTheta 
        self.point1[2] = y*cosTheta + x*sinTheta
        
        x = self.point2[1]
        y = self.point2[2]
        self.point2[1] = x*cosTheta -y*sinTheta 
        self.point2[2] = y*cosTheta + x*sinTheta
        
        x = self.point3[1]
        y = self.point3[2]
        self.point3[1] = x*cosTheta -y*sinTheta 
        self.point3[2] = y*cosTheta + x*sinTheta
        
        x = self.point4[1]
        y = self.point4[2]
        self.point4[1] = x*cosTheta -y*sinTheta 
        self.point4[2] = y*cosTheta + x*sinTheta
        
        x = self.point5[1]
        y = self.point5[2]
        self.point5[1] = x*cosTheta -y*sinTheta 
        self.point5[2] = y*cosTheta + x*sinTheta
        
        x = self.point6[1]
        y = self.point6[2]
        self.point6[1] = x*cosTheta -y*sinTheta 
        self.point6[2] = y*cosTheta + x*sinTheta
        
        x = self.point7[1]
        y = self.point7[2]
        self.point7[1] = x*cosTheta -y*sinTheta 
        self.point7[2] = y*cosTheta + x*sinTheta
        
        x = self.point8[1]
        y = self.point8[2]
        self.point8[1] = x*cosTheta -y*sinTheta 
        self.point8[2] = y*cosTheta + x*sinTheta

    def rotateY(self, degree):
        sinTheta = math.sin(degree)
        cosTheta = math.cos(degree)
        x = self.point1[0]
        y = self.point1[2]
        self.point1[0] = x*cosTheta -y*sinTheta 
        self.point1[2] = y*cosTheta + x*sinTheta
        
        x = self.point2[0]
        y = self.point2[2]
        self.point2[0] = x*cosTheta -y*sinTheta 
        self.point2[2] = y*cosTheta + x*sinTheta
        
        x = self.point3[0]
        y = self.point3[2]
        self.point3[0] = x*cosTheta -y*sinTheta 
        self.point3[2] = y*cosTheta + x*sinTheta
        
        x = self.point4[0]
        y = self.point4[2]
        self.point4[0] = x*cosTheta -y*sinTheta 
        self.point4[2] = y*cosTheta + x*sinTheta
        
        x = self.point5[0]
        y = self.point5[2]
        self.point5[0] = x*cosTheta -y*sinTheta 
        self.point5[2] = y*cosTheta + x*sinTheta
        
        x = self.point6[0]
        y = self.point6[2]
        self.point6[0] = x*cosTheta -y*sinTheta 
        self.point6[2] = y*cosTheta + x*sinTheta
        
        x = self.point7[0]
        y = self.point7[2]
        self.point7[0] = x*cosTheta -y*sinTheta 
        self.point7[2] = y*cosTheta + x*sinTheta
        
        x = self.point8[0]
        y = self.point8[2]
        self.point8[0] = x*cosTheta -y*sinTheta 
        self.point8[2] = y*cosTheta + x*sinTheta


def setToMiddle(pos,flag):
    if(flag == 0):
        return(xSize/2 + pos)
    if(flag == 1):
        return(ySize/2-pos)



    
    
top = tkinter.Tk()
c = tkinter.Canvas(top,bg ="white",height = 500, width = 500)
def hello():
    print ("hello!")



label1 = tkinter.Label(top,text="X Rotate: ")
label1.pack()
wText = tkinter.Entry(top)
wText.pack()
wText.insert(0,"0")
label2 = tkinter.Label(top,text="Y Rotate: ")
label2.pack()
xText = tkinter.Entry(top)
xText.pack()
xText.insert(0,"0")
label3 = tkinter.Label(top,text="Z Rotate: ")
label3.pack()
yText = tkinter.Entry(top)
yText.pack()
yText.insert(0,"0") 
"""Testing Side"""
cube1 = cube()
square = cube1.getFrontSide()
i = 0
for x in square:
    square[i] = setToMiddle(x,i%2)
    i = i+1
c.create_line(square)
c.pack()
"""Testing Rotate"""

while(True):
    rotX = wText.get()
    rotY = xText.get()
    rotZ = yText.get()
    if(not rotX.isnumeric()):
        rotX = 0
    if(not rotY.isnumeric()):
        rotY = 0
    if(not rotZ.isnumeric()):
        rotZ = 0
    
    c.delete('all')
    time.sleep(1/144)

    cube1.rotateZ(float(rotZ)/144)
    cube1.rotateX(float(rotX)/144)
    cube1.rotateY(float(rotY)/144)
    
        
    Front = cube1.getFrontSide()
    Left = cube1.getLeftSide()
    Right = cube1.getRightSide()
    Bottom = cube1.getBottomSide()
    TopS = cube1.getTopSide()
    Back = cube1.getBackSide()
    
        
        
    
    
    i = 0
    for x in Front:
        Front[i] = setToMiddle(x,i%2)
        i = i+1
    i = 0
    for x in Left:
        Left[i] = setToMiddle(x,i%2)
        i = i+1
    i = 0
    for x in Right:
        Right[i] = setToMiddle(x,i%2)
        i = i+1
    i = 0
    for x in Bottom:
        Bottom[i] = setToMiddle(x,i%2)
        i = i+1
    i = 0
    for x in TopS:
        TopS[i] = setToMiddle(x,i%2)
        i = i+1
    i = 0
    for x in Back:
        Back[i] = setToMiddle(x,i%2)
        i = i+1
    sort = cube1.colorOrder()
    for x in range(6):
        if sort[x] == cube1.getFrontSideZAvg():
            c.create_polygon(Front,fill="red")
        if sort[x] == cube1.getLeftSideZAvg():
            c.create_polygon(Left,fill = "green")
        if sort[x] == cube1.getRightSideZAvg():
            c.create_polygon(Right,fill="blue")
        if sort[x] == cube1.getBottomSideZAvg():
            c.create_polygon(Bottom, fill="yellow")
        if sort[x] == cube1.getTopSideZAvg():
            c.create_polygon(TopS,fill="cyan")
        if sort[x] == cube1.getBackSideZAvg():
            c.create_polygon(Back,fill="orange")
        
    """c.create_polygon(Front,fill="red")
    c.create_polygon(Left,fill = "#1f1")
    c.create_polygon(Right,fill="blue")
    c.create_polygon(Bottom)
    c.create_polygon(TopS)
    c.create_polygon(Back,fill="orange")
"""
    
    c.pack()
    top.update()

    

top.mainloop()
 