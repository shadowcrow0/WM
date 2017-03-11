from random import sample
import glob, os, sys, time
from psychopy import core, event, gui, visual, data, info
#####################background######################################


info = {'cond':['2000ms','1000ms'],'ID':'', 'age':'','gender':['Male','Female'], 'IntruC':['.3','2']}
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title = 'VisualWorkingMemory', 
                          order = ['ID','cond','age'])
if infoDlg.OK == False:
    core.quit()

from random import sample, shuffle
import sys, time
from psychopy import core, event, gui, visual, data, info

#monitorunittools to convert cm<->pix<->deg etc. 

#1.0 define 8 pos
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
p1 = [100, 200]
p2 = [100, -200]
p3 = [-100, 200]
p4 = [200, 100]
p5 = [200, -100]
p6 = [-200, 100]
p7 = [-200, -100]
p8 = [-100, -200]
#1.1 setting  background = gery
WIN = visual.Window((800, 600), color="grey", units="pix")
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'grey')
FIX = visual.TextStim(WIN, text='+', height=40, color='white', pos=(0, 0))
COLORS = ['white', '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'dark-blue-green']
t = (.3,2.0)
Ts = sample(t,2)
positions = sample(POSITIONS,2)
pos_catA = sample(positions,1)
res_catA = sample(pos_catA,1)
pos_catB =list(set(positions) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS[1:],2)
col_else = list(set(COLORS[1:])-set(colors))
col_new = sample(col_else[1:],1)
#################setsize 1
def NEX():
    next= visual.TextStim(WIN,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    WIN.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    FIX.draw()
    WIN.flip()
    core.wait(.5)
def squ2():
    squares = [] #列出一個空矩陣準備之後要畫的形狀
    for i in range(2):
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(colors[idx])
            squ.setPos(positions[idx])
            squ.draw()
def catA_cue1():#同時出現圓形跟菱形在特定位置
    circles = []#產生之後要畫圓形矩陣
    diamonds= []#菱形
    for i in range(1):#這邊只要出現一個圓形
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')#設定要出現圓形的大小跟顏色
        circles.append(cir)#把 cir 加到circles之後
        for idx, squ in enumerate(circles):
            #print(idx)
            cir.setPos(pos_catA[idx])#套用到指定位置
            cir.draw()
    for i in range(1):
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )#畫個菱形
        diamonds.append(diam) #加到菱形矩陣
        for idx, squ in enumerate(diamonds):
            diam.setPos(pos_catA[idx])#套用菱形應該出現的矩陣
            diam.draw()
def catB_cue1():#出現圓形在特定位置
    circles = []
    for i in range(1):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        circles.append(cir)
        for idx, squ in enumerate(circles):
            cir.setPos(pos_catB[idx])
            cir.draw()
def catA():#產生圓形跟菱形作為提示，方形作為刺激
  #################與cue_catA重複######################
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
            #############################結束
    squares = []
    for i in range(1):#畫出方形的顏色跟位置
        squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
        squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(col_else[idx])
            #divide 3 condtions
            squ.setPos(res_catA[idx])
            squ.draw()
def catB():#產生圓形作為提示，方形作為刺激
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
def RT():#計算反應時間
    t1 = core.getTime()
    Ans = event.waitKeys(keyList = ['k','s'])
    t2 = core.getTime()
    RT1 = t2-t1
def stimBA():
    positions = sample(POSITIONS,2)#從l21 挑出兩個位置作為這次呈現目標
    pos_catA = sample(positions,1)#圓形加菱形這次要出現的位置
    res_catA = sample(pos_catA,1)#設定讓受試者判斷的時候會出現圓形菱形+方塊的位置
    pos_catB =list(set(positions) - set(pos_catA)) #設定圓形出現位置
    res_catB = sample(pos_catB,1)#設定讓受試者判斷出現圓形+方塊的位置
    colors = sample(COLORS[1:],2)#從l35 挑出兩個出現的顏色
    col_else = list(set(COLORS[1:])-set(colors))#選擇之前沒選到顏色到這個變數
    col_new = sample(col_else[1:],1)#隨機選定一個顏色變數
    squ2()#畫好刺激要用的方形
    catA_cue1()#設定畫好圓形跟菱形的提示
    catB_cue1()#設定且畫好菱形的提示
    WIN.flip()#將上述三者推出螢幕
    core.wait(2)#在螢幕中呈現兩秒鐘
    catB_cue1()#畫出圓形的提示
    WIN.flip()#讓菱形提示呈現在螢幕
    core.wait(Ts[1])#並等待 Ts
    catB()#畫出菱形的提示加上色塊
    WIN.flip() #讓受試者判斷菱形出現的顏色跟最一開始 l146 一樣否
    RT()#計算反應時間跟受試者作答內容
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
stimAB()
