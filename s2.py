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
def NEX():
    next= visual.TextStim(WIN,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    WIN.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    FIX.draw()
    WIN.flip()
    core.wait(.5)
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
    NEX()
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
    NEX()
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

