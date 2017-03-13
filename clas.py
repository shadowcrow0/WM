import numpy as np
from random import sample, shuffle, randint
import sys, time
from psychopy import core, event, gui, visual, data, info


WIN = visual.Window((800, 600), color="grey", units="pix")
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=40, color='white', pos=(0, 0))
COLORS = [ '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'blue']
t = (.3,2.0)

class image():
    def __inti__(self, WIN, ALERT_MSG, FIX,Ts):
        self.p_1 = [100, 200]
        self.p_2 = [100, -200]
        self.p_3 = [-100, 200]
        self.p_4 = [200, 100]
        self.p_5 = [200, -100]
        self.p_6 = [-200, 100]
        self.p_7 = [-200, -100]
        self.p_8 = [-100, -200]
        ####calculate distance
        self.p1 = np.array(p_1)
        self.p2 = np.array(p_2)
        self.p3 = np.array(p_3)
        self.p4 = np.array(p_4)
        self.p5 = np.array(p_5)
        self.p6 = np.array(p_6)
        self.p7 = np.array(p_7)
        self.p8 = np.array(p_8)
        self.COLORS = [ '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'blue']
        self.POSITIONS= [p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8]
        self.WIN = WIN
        self.ALERT_MSG=visual.TextStim(WIN, pos=(0, 4), height=30,                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
        self.FIX =visual.TextStim(WIN, text='+', height=40, color='white', pos=(0, 0))
        self.NEX= NEX()
        self.Ts4 = sample([0.3,2.0],2)
        self.pos_catA4 = sample(POSITIONS4,4)
        self.res_catA4 = sample(pos_catA4,1)
        self.pos_catB4 =list(set(POSITIONS) - set(pos_catA4))
        self.res_catB4 = sample(pos_catB4,1)
        self.colors4 = sample(COLORS,8)
        self.col_catA4 = sample(colors4,4)
        self.col_catB4 = list(set(colors4)-set(col_catA4))
        self.col_else4 = list(set(COLORS)-set(colors4))
        self.col_new4 = sample(col_else4,4)
        self.col_int4 = sample(colors4,4)
        self.Ts3 = sample([0.3,2.0],2)
        self.positions3 = sample(POSITIONS3,6)
        self.pos_catA3 = sample(positions3,3)
        self.res_catA3 = sample(pos_catA3,1)
        self.pos_catB3 =list(set(positions3) - set(pos_catA3))
        self.res_catB3 = sample(pos_catB3,1)
        self.colors3 = sample(COLORS,6)
        self.col_catA3 = colors3[:2]
        self.col_catB3 = list(set(COLORS)- set(col_catA))
        self.col_else3 = list(set(COLORS[1:])-set(colors3))
        self.col_new3 = sample(col_else3,3)
        self.col_catA3 = sample(colors4,3)
        self.col_catB3 = list(set(colors3)-set(col_catA3))
        self.Ts2 = sample([0.3,2.0],2)
        self.positions2 = sample(POSITIONS,4)
        self.pos_catA2 = sample(positions2,2)
        self.res_catA2 = sample(pos_catA2,1)
        self.pos_catB2 =list(set(positions2) - set(pos_catA2))
        self.res_catB2 = sample(pos_catB2,1)
        self.colors2 = sample(COLORS,4)
        self.col_else2 = list(set(COLORS)-set(colors2))
        self.col_new2 = sample(col_else2,2)
        self.col_catA2 = sample(colors2,4)
        self.col_catB2 = list(set(colors2)-set(col_catA2))
        self.positions1 = sample(POSITIONS,2)
        self.pos_catA1 = sample(positions1,1)
        self.res_catA1 = sample(pos_catA1,1)
        self.pos_catB1 =list(set(positions1) - set(pos_catA1))
        self.res_catB1 = sample(pos_catB1,1)
        self.colors1 = sample(COLORS,2)
        self.col_else1 = list(set(COLORS)-set(colors1))
        self.col_new1 = sample(col_else1,1)
        self.col_catA1 = sample(colors1,1)
        self.col_catB1 = list(set(colors1)-set(col_catA1))
        self.Ts1 = sample([0.3,2.0],2)
        self.dist1_1 = np.linalg.norm(p1 - p1)
        self.dist1_2 = np.linalg.norm(p1 - p2)
        self.dist1_3 = np.linalg.norm(p1 - p3)
        self.dist1_4 = np.linalg.norm(p1 - p4)
        self.dist1_5 = np.linalg.norm(p1 - p5)
        self.dist1_6 = np.linalg.norm(p1 - p6)
        self.dist1_7 = np.linalg.norm(p1 - p7)
        self.dist1_8 = np.linalg.norm(p1 - p8)
        ####dist2
        self.dist2_1 = np.linalg.norm(p2 - p1)
        self.dist2_2 = np.linalg.norm(p2 - p2)
        self.dist2_3 = np.linalg.norm(p2 - p3)
        self.dist2_4 = np.linalg.norm(p2 - p4)
        self.dist2_5 = np.linalg.norm(p2 - p5)
        self.dist2_6 = np.linalg.norm(p2 - p6)
        self.dist2_7 = np.linalg.norm(p2 - p7)
        self.dist2_8 = np.linalg.norm(p2 - p8)
        #####dist3
        self.dist3_1 = np.linalg.norm(p3 - p1)
        self.dist3_2 = np.linalg.norm(p3 - p2)
        self.dist3_3 = np.linalg.norm(p3 - p3)
        self.dist3_4 = np.linalg.norm(p3 - p4)
        self.dist3_5 = np.linalg.norm(p3 - p5)
        self.dist3_6 = np.linalg.norm(p3 - p6)
        self.dist3_7 = np.linalg.norm(p3 - p7)
        self.dist3_8 = np.linalg.norm(p3 - p8)
        #####p4
        self.dist4_1 = np.linalg.norm(p4 - p1)
        self.dist4_2 = np.linalg.norm(p4 - p2)
        self.dist4_3 = np.linalg.norm(p4 - p3)
        self.dist4_4 = np.linalg.norm(p4 - p4)
        self.dist4_5 = np.linalg.norm(p4 - p5)
        self.dist4_6 = np.linalg.norm(p4 - p6)
        self.dist4_7 = np.linalg.norm(p4 - p7)
        self.dist4_8 = np.linalg.norm(p4 - p8)
        #####p5
        self.dist5_1 = np.linalg.norm(p5 - p1)
        self.dist5_2 = np.linalg.norm(p5 - p2)
        self.dist5_3 = np.linalg.norm(p5 - p3)
        self.dist5_4 = np.linalg.norm(p5 - p4)
        self.dist5_5 = np.linalg.norm(p5 - p5)
        self.dist5_6 = np.linalg.norm(p5 - p6)
        self.dist5_7 = np.linalg.norm(p5 - p7)
        self.dist5_8 = np.linalg.norm(p5 - p8)
        #####p6
        self.dist6_1 = np.linalg.norm(p6 - p1)
        self.dist6_2 = np.linalg.norm(p6 - p2)
        self.dist6_3 = np.linalg.norm(p6 - p3)
        self.dist6_4 = np.linalg.norm(p6 - p4)
        self.dist6_5 = np.linalg.norm(p6 - p5)
        self.dist6_6 = np.linalg.norm(p6 - p6)
        self.dist6_7 = np.linalg.norm(p6 - p7)
        self.dist6_8 = np.linalg.norm(p6 - p8)
        #####p7
        self.dist7_1 = np.linalg.norm(p7- p1)
        self.dist7_2 = np.linalg.norm(p7- p2)
        self.dist7_3 = np.linalg.norm(p7- p3)
        self.dist7_4 = np.linalg.norm(p7- p4)
        self.dist7_5 = np.linalg.norm(p7- p5)
        self.dist7_6 = np.linalg.norm(p7- p6)
        self.dist7_7 = np.linalg.norm(p7- p7)
        self.dist7_8 = np.linalg.norm(p7- p8)
        #####p8
        self.dist8_1 = np.linalg.norm(p8 - p1)
        self.dist8_2 = np.linalg.norm(p8 - p2)
        self.dist8_3 = np.linalg.norm(p8 - p3)
        self.dist8_4 = np.linalg.norm(p8 - p4)
        self.dist8_5 = np.linalg.norm(p8 - p5)
        self.dist8_6 = np.linalg.norm(p8 - p6)
        self.dist8_7 = np.linalg.norm(p8 - p7)
        self.dist8_8 = np.linalg.norm(p8 - p8)
        self.catA= catA()
    def catA():
        circles = []
        diamonds= []
        for i in range(1):
            cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
            circles.append(cir)
            for idx, squ in enumerate(circles):
                cir.setPos(res_catA1[idx])
                cir.draw()
        for i in range(1):
            diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
            diamonds.append(diam)
            for idx, squ in enumerate(diamonds):
                diam.setPos(res_catA1[idx])
                diam.draw()
        squares = []
        for i in range(1):
            squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
            squares.append(squ)
            for idx, squ in enumerate(squares):
                squ.setFillColor(col_else1[idx])
                #divide 3 condtions
                squ.setPos(res_catA1[idx])
                squ.draw()
    def catB():
        circles = []
        for i in range(1):
            cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
            circles.append(cir)
            for idx, squ in enumerate(circles):
                cir.setPos(pos_catB1[idx])
                cir.draw()
        squares = []
        for i in range(1):
            squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
            squares.append(squ)
            for idx, squ in enumerate(squares):
                squ.setFillColor(col_new1[idx])
                squ.setPos(pos_catB1[idx])
                squ.draw()
    def RT():
        t1 = core.getTime()
        Ans = event.waitKeys(keyList = ['k','s'])
        t2 = core.getTime()
        RT1 = t2-t1
    catA()
    WIN.flip()
    core.wait(Ts1[0])
    image() 
def NEX():
    next= visual.TextStim(WIN,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    WIN.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    FIX.draw()
    WIN.flip()
    core.wait(.5)
