
from random import sample, shuffle, randint
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
circles = []
diamonds= []
squares= []

pos_catA=[]
pos_catA = sample(POSITIONS,4)
res_catA = sample(pos_catA,1)
pos_catB =list(set(POSITIONS) - set(pos_catA))
res_catB = sample(pos_catB,1)
colors = sample(COLORS,8)
col_else = list(set(COLORS)-set(colors))
col_new = sample(col_else[1:],4)
locations = POSITIONS
COLS=colors
def squBuilder(positions):
    squares=[]
    for pos in positions:
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squ.setPos(pos)
        squares.append(squ)
    return squares
def cir_build():
    circles=[]
    for pos in positions:
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        cir.setPos(pos)
        circles.append(cir)
    return circles
def diam_biuld():
    diamonds=[]
    for pos in positions:
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diam.setPos(pos)
        diamonds.append(diam)
    return diamonds
def set():
    for i in range(4):
        positions = positions_builder(i)
        squares = square_builder(positions)
        positions_a = sample(positions, i/2)
        positions_b = set(positions)-set(positions_a)
        a_shape = a_diagram_builder(positions_a)
        b_shape = b_diagram_builder(positions_b)

#// first time
run(positions, positions_a, positions_b)
#// second time
run(positions, positions_a, positions_b)
'u' 
def positions_builder(i):
    positions_array=[]
    for i in range(4):
        positions_array.append(sample(POSITIONS,i))
    return positions_array

positions_builder()
def square_builder(positions=):
    for idx in positions_array:
        squBuilder()
        squares.setPos(positions_array[idx])
    #// 根據座標產生方形並回傳方形array
    return square_array
