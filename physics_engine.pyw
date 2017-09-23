from graphics import *
from time import sleep
from random import randint
from math import *
MAXX = 800
MAXY = 800
win = GraphWin('Physics', MAXX, MAXY)
win.setBackground('white')

colors = ['red', 'blue', 'green', 'black', 'orange']

radius = 20

grav = 0.05 #default = 0.05

LEN = 0
circles = [None] * LEN

class Ball:
    def __init__(self, x, y, init_s_x, init_s_y, color):
        self.sX = init_s_x
        self.sY = init_s_y
        self.x = x
        self.y = y
        self.c = Circle(Point(x, y), radius)
        self.color = color
        self.hit = False
        self.hitOld = False

    def move(self):
        self.x = self.x + self.sX
        self.y = self.y + self.sY

    def update(self, index, check):
        if check:
            for i in range(len(circles)):
                if index != i:
                    if sqrt(pow(abs(self.x - circles[i].x), 2) + pow(abs(self.y - circles[i].y), 2)) <= radius * 2: # If collision has happened with other ball
                        self.sX = circles[i].sX
                        self.sY = circles[i].sY
                        
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
    circles[i] = Ball(randint(0, MAXX), randint(0, MAXY), randint(-10, 10), randint(-10, 10), colors[randint(0, 4)])

u = 0

while True:
    for i in range(len(circles)):
        circles[i].update(i, True)
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
        win.getKey()
        
    pt1 = win.checkMouse()
    if pt1 != None:
        pt2 = win.getMouse()
        l = Line(pt1, pt2)
        l.setWidth(3)
        l.setFill('red')
        l.draw(win)
        newBall = Ball(int(pt1.getX()), int(pt1.getY()), int((pt1.getX() - pt2.getX()) / 20), int((pt1.getY() - pt2.getY()) / 20), colors[randint(0, 4)])
        circles.append(newBall)
        sleep(0.1)
        l.undraw()
    sleep(0.01)









