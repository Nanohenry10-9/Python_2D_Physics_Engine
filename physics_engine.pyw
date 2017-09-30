from graphics import *
from time import sleep
from random import randint
from math import *
MAXX = 800
MAXY = 800
win = GraphWin('Physics', MAXX, MAXY)
win.setBackground('white')

colors = ['red', 'blue', 'green', 'black', 'orange']

radius = input("Ball radius? ")
if not radius.isdigit():
    radius = 20
else:
    radius = int(radius)
doCollision = input("Do collision detection? ")
if doCollision == "true" or doCollision == "True" or doCollision == '1':
    doCollision = True
else:
    doCollision = False

grav = 0.05

LEN = 0
circles = [None] * LEN

class Ball:
    def __init__(self, x, y, init_s_x, init_s_y, color, mass):
        self.sX = init_s_x
        self.sY = init_s_y
        self.x = x
        self.y = y
        self.c = Circle(Point(x, y), radius)
        self.color = color
        self.hit = False
        self.hitOld = False
        self.mass = mass

    def inside(self):
        for i in range(len(circles)):
            if sqrt(pow(abs(self.x - circles[i].x), 2) + pow(abs(self.y - circles[i].y), 2)) < radius * 2 and sqrt(pow(abs(self.x - circles[i].x), 2) + pow(abs(self.y - circles[i].y), 2)) != 0:
                return i
        return -1

    def move(self):
        self.x = self.x + self.sX
        self.y = self.y + self.sY

    def update(self, index, check):
        if check:
            i = self.inside()
            if i != -1:
                while self.inside() != -1:
                    tempX = (circles[i].x - self.x) / (radius * 1.5)
                    tempY = (circles[i].y - self.y) / (radius * 1.5)
                    self.sX = (self.x - circles[i].x) / (radius * 1.5)
                    self.sY = (self.y - circles[i].y) / (radius * 1.5)
                    circles[i].sX = tempX
                    circles[i].sY = tempY
                    self.move()
                    circles[i].move()

        self.sY = self.sY + grav
        if self.y + radius >= MAXY:
            self.y = MAXY - radius
            self.sY = self.sY * -0.7
            self.sX = self.sX * 0.9
        if self.x + radius >= MAXX:
            self.x = MAXX - radius
            self.sX = self.sX * -0.9
        if self.x - radius <= 0:
            self.x = 0 + radius
            self.sX = self.sX * -0.9

    def drawBall(self):
        self.c.undraw()
        self.c = Circle(Point(self.x, self.y), radius)
        self.c.setFill(self.color)
        self.c.draw(win)

for i in range(LEN):
    circles[i] = Ball(randint(0, MAXX), randint(0, MAXY), randint(-10, 10), randint(-10, 10), colors[randint(0, 4)], radius)

u = 0

while True:
    for i in range(len(circles)):
        circles[i].update(i, doCollision)
        circles[i].move()

    if u == 0:
        for i in range(len(circles)):
            circles[i].drawBall()
    u = u + 1
    if u == 2:
        u = 0
        
    key = win.checkKey()
    if key == 'd':
        if len(circles) > 0:
            del circles[-1]
    elif key == 's':
        key = win.getKey()
        if key == 's':
            break
        
    pt1 = win.checkMouse()
    if pt1 != None:
        pt2 = win.getMouse()
        l = Line(pt1, pt2)
        l.setWidth(3)
        l.setFill('red')
        l.draw(win)
        newBall = Ball(int(pt1.getX()), int(pt1.getY()), int((pt1.getX() - pt2.getX()) / 20), int((pt1.getY() - pt2.getY()) / 20), colors[randint(0, 4)], radius)
        circles.append(newBall)
        sleep(0.1)
        l.undraw()
    sleep(0.01)









