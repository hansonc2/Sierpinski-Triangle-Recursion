##############################################################################
#A recursive program that draws
#Cole Hanson
##############################################################################

from graphics import *
import sys

def drawFractal(win,length, detail, x, y):
    """a recursive function that draws 3 triangles in each detail level beyond 0"""
    #defines three points in each triangle
    tripoints = [Point(x,y), Point((x+length),y),Point(x + length/2,(y+length))]
    tri = Polygon(tripoints)
    #base case that stops recusrion when detail level is 0
    if detail == 0:
        tri.draw(win)
        return
    #recersive call that puts three triangles within the last detail level
    else:
        drawFractal(win,.5 * length, detail-1, x, y)
        drawFractal(win,.5 * length, detail-1, x + length/2, y)
        drawFractal(win,.5 * length,detail-1,x + length/4,y + length/2)


def main():
    #takes triangle length and detail level as command line arguments
    length = int(sys.argv[1])
    detail = int(sys.argv[2])
    #creates a window for the fractals to be drawn
    win = GraphWin("TriFractals", 1000, 1000)
    drawFractal(win,length,detail,100,100)
    #input function to end the program
    q = input("PRESS ENTER TO QUIT")

if __name__ == "__main__":
    main()
