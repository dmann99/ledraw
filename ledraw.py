from graphics import *

class ledraw:
    xSize=0
    ySize=0

    elementSize=20
    elementPad=5

    matrix = []

    def __init__(self, xSize=8, ySize=8):
        print('Creating an ',xSize,' x ', ySize,' matrix')
        self.xSize=xSize
        self.ySize=ySize


        winXSize=xSize*(self.elementSize+self.elementPad)-15
        winYSize=ySize*(self.elementSize+self.elementPad)-15
        print(winXSize,winYSize)

        win = GraphWin('Test Click Events and Objects', winXSize, winYSize)
        win.setBackground('black')

        for x in range(0,xSize):
            self.matrix.append([])

        for x in range(0,xSize):
            for y in range(0,ySize):
                xMin=(x*self.elementSize)+self.elementPad
                xMax=(x*self.elementSize)+self.elementSize
                yMin=(y*self.elementSize)+self.elementPad
                yMax=(y*self.elementSize)+self.elementSize
                NewRect=Rectangle(Point(xMin,yMin),Point(xMax,yMax))
                NewRect.setFill('red')
                NewRect.draw(win)
                #self.matrix[y].append(NewRect)

        win.getMouse()



temp=ledraw(8,3)






