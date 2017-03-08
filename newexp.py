from random import sample, shuffle, randint
import sys, time
from psychopy import core, event, gui, visual, data, info

#monitorunittools to convert cm<->pix<->deg etc. 

#1.0 define 8 pos
POSITIONS =[]
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
p1 = [100, 200]
p2 = [100, -200]
p3 = [-100, 200]
p4 = [200, 100]
p5 = [200, -100]
p6 = [-200, 100]
p7 = [-200, -100]
p8 = [-100, -200]
P = [p1,p2,p3,p4,p5,p6,p7,p8]
#1.1 setting  background = gery
WIN = visual.Window((800, 600), color="grey", units="pix")
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=40, color='white', pos=(0, 0))
COLORS = ['white', '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'blue']
t = (.3,2.0)
Ts = sample(t,2)
pos_catA=[]
pos_catA = sample(POSITIONS,4)
res_catA = sample(pos_catA,1)
pos_catB =list(set(POSITIONS) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS[1:],8)
col_else = list(set(COLORS[1:])-set(colors))
col_new = sample(col_else[1:],4)
class varis:
    def __inti__(self, Ts, pos_catA, pos_catB, res_catA, res_catB, FIX, COLORS, ALERT_MSG, WIN, colors, col_else,col_new, POSITIONS):
        self.Ts = Ts
        self.POSITIONS = POSITIONS
        self.pos_catA = pos_catA
        self.pos_catB = pos_catB
        self.res_catA = res_catA
        self.res_catB = res_catB
        self.FIX = FIX
        self.WIN = WIN
        self.colors = colors
        self.ALERT_MSG = ALERT_MSG
        self.col_else = col_else
        self.col_new = col_new
def NEX():
    next= visual.TextStim(WIN,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    WIN.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    FIX.draw()
    WIN.flip()
    core.wait(.5)
NEX()
#draw 8 suqare, fillin black
def squ():
    squares = []
    for i in range(8):
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(colors[idx])
            squ.setPos(POSITIONS[idx])
            squ.draw()
def catA_cue():
    circles = []
    diamonds= []
    for i in range(4):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(pos_catA[idx])
            cir.draw()
    for i in range(4):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diamonds.append(diam)
        for idx, squ in enumerate(diamonds):
            diam.setPos(pos_catA[idx])
            diam.draw()

def catB_cue():
    circles = []
    for i in range(4):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()
def catA():
    circles = []
    diamonds= []
    for i in range(1):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(res_catA[idx])
            cir.draw()
    for i in range(1):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diamonds.append(diam)
        for idx, squ in enumerate(diamonds):
            diam.setPos(res_catA[idx])
            diam.draw()
    squares = []
    for i in range(1):
        squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(col_else[idx])
            #divide 3 condtions
            squ.setPos(res_catA[idx])
            squ.draw()
def catB():
    circles = []
    for i in range(1):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()
    squares = []
    for i in range(1):
        squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(col_new[idx])
            squ.setPos(pos_catB[idx])
            squ.draw()
def RT():
    t1 = core.getTime()
    Ans = event.waitKeys(keyList = ['k','s'])
    t2 = core.getTime()
    RT1 = t2-t1

def stimBA4():
    pos_catA=[]
    pos_catA = sample(POSITIONS,4)
    res_catA = sample(pos_catA,1)
    pos_catB =list(set(POSITIONS) - set(pos_catA))
    res_catB = sample(pos_catB,1)
    colors = sample(COLORS[1:],8)
    col_else = list(set(COLORS[1:])-set(colors))
    col_new = sample(col_else[1:],4)
    squ()
    catA_cue()
    catB_cue()
    WIN.flip()
    core.wait(2)
    catB_cue()
    WIN.flip()
    core.wait(Ts[1])
    catB()
    WIN.flip()
    RT()
    catA_cue()
    WIN.flip()
    core.wait(Ts[0])
    catA()
    WIN.flip()
    RT()



def stimAB4():
    pos_catA=[]
    pos_catA = sample(POSITIONS,4)
    res_catA = sample(pos_catA,1)
    pos_catB =list(set(POSITIONS) - set(pos_catA))
    res_catB = sample(pos_catB,1)
    colors = sample(COLORS[1:],8)
    col_else = list(set(COLORS[1:])-set(colors))
    col_new = sample(col_else[1:],4)
    squ()
    catA_cue()
    catB_cue()
    WIN.flip()
    core.wait(2)
    catA_cue()
    WIN.flip()
    core.wait(Ts[0])
    catA()
    WIN.flip()
    RT()
    catB_cue()
    WIN.flip()
    core.wait(Ts[1])
    catB()
    WIN.flip()
    RT()
#stimBA4()
#stimAB4()
###################################################SETSIZE3####################################
positions = sample(POSITIONS,6)
pos_catA = sample(positions,3)
res_catA = sample(pos_catA,1)
pos_catB =list(set(positions) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS[1:],6)
col_else = list(set(COLORS[1:])-set(colors))
col_new = sample(col_else[1:],3)
def squ6():
    squares = []
    for i in range(6):
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(colors[idx])
            squ.setPos(positions[idx])
            squ.draw()
def catA_cue3():
    circles = []
    diamonds= []
    for i in range(3):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(pos_catA[idx])
            cir.draw()
    for i in range(3):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diamonds.append(diam)
        for idx, squ in enumerate(diamonds):
            diam.setPos(pos_catA[idx])
            diam.draw()
def catB_cue3():
    circles = []
    for i in range(3):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()

def stimBA3():
    squ6()
    catA_cue3()
    catB_cue3()
    WIN.flip()
    core.wait(2)
    catB_cue3()
    WIN.flip()
    core.wait(Ts[1])
    catB()
    WIN.flip()
    RT()
    catA_cue3()
    WIN.flip()
    core.wait(Ts[0])
    catA()
    WIN.flip()
    RT()
def stimAB3():
    squ6()
    catA_cue3()
    catB_cue3()
    WIN.flip()
    core.wait(2)
    catA_cue3()
    WIN.flip()
    core.wait(Ts[1])
    catA()
    WIN.flip()
    RT()
    catB_cue3()
    WIN.flip()
    core.wait(Ts[0])
    catB()
    WIN.flip()
    RT()
#stimAB3()
positions = sample(POSITIONS,4)
pos_catA = sample(positions,2)
res_catA = sample(pos_catA,1)
pos_catB =list(set(positions) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS[1:],4)
col_else = list(set(COLORS[1:])-set(colors))
col_new = sample(col_else[1:],2)
#################setsize 2
def squ4():
    squares = []
    for i in range(4):
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(colors[idx])
            squ.setPos(positions[idx])
            squ.draw()
def catA_cue2():
    circles = []
    diamonds= []
    for i in range(2):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(pos_catA[idx])
            cir.draw()
    for i in range(2):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diamonds.append(diam)
        for idx, squ in enumerate(diamonds):
            diam.setPos(pos_catA[idx])
            diam.draw()
def catB_cue2():
    circles = []
    for i in range(2):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()
def stimBA2():
    squ4()
    catA_cue2()
    catB_cue2()
    WIN.flip()
    core.wait(2)
    catB_cue2()
    WIN.flip()
    core.wait(Ts[1])
    catB()
    WIN.flip()
    RT()
    catA_cue2()
    WIN.flip()
    core.wait(Ts[0])
    catA()
    WIN.flip()
    RT()
def stimAB2():
    squ4()
    catA_cue2()
    catB_cue2()
    WIN.flip()
    core.wait(2)
    catA_cue2()
    WIN.flip()
    core.wait(Ts[1])
    catA()
    WIN.flip()
    RT()
    catB_cue2()
    WIN.flip()
    core.wait(Ts[0])
    catB()
    WIN.flip()
    RT()
#stimAB2()
#stimBA2()
positions = sample(POSITIONS,2)
pos_catA = sample(positions,1)
res_catA = sample(pos_catA,1)
pos_catB =list(set(positions) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS[1:],2)
col_else = list(set(COLORS[1:])-set(colors))
col_new = sample(col_else[1:],1)
#################setsize 1
def squ2():
    squares = []
    for i in range(2):
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(colors[idx])
            squ.setPos(positions[idx])
            squ.draw()
def catA_cue1():
    circles = []
    diamonds= []
    for i in range(1):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(pos_catA[idx])
            cir.draw()
    for i in range(1):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diamonds.append(diam)
        for idx, squ in enumerate(diamonds):
            diam.setPos(pos_catA[idx])
            diam.draw()
def catB_cue1():
    circles = []
    for i in range(1):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()

def stimBA():
    positions = sample(POSITIONS,2)
    pos_catA = sample(positions,1)
    res_catA = sample(pos_catA,1)
    pos_catB =list(set(positions) - set(pos_catA))
    res_catB = sample(pos_catB,1)
    colors = sample(COLORS[1:],2)
    col_else = list(set(COLORS[1:])-set(colors))
    col_new = sample(col_else[1:],1)
    squ2()
    catA_cue1()
    catB_cue1()
    WIN.flip()
    core.wait(2)
    catB_cue1()
    WIN.flip()
    core.wait(Ts[1])
    catB()
    WIN.flip()
    RT()
    catA_cue1()
    WIN.flip()
    core.wait(Ts[0])
    catA()
    WIN.flip()
    RT()
def stimAB():
    squ2()
    catA_cue1()
    catB_cue1()
    WIN.flip()
    core.wait(2)
    catA_cue1()
    WIN.flip()
    core.wait(Ts[1])
    catA()
    WIN.flip()
    RT()
    catB_cue1()
    WIN.flip()
    core.wait(Ts[0])
    catB()
    WIN.flip()
    RT()
#stimBA()
#stimAB()
