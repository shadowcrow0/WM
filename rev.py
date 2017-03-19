#for AWON
#
#from random import sample, shuffle, randint
#import sys, time
#from psychopy import core, event, gui, visual, data, info
#
#
# init variable
#DEF_POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
#CASES =[1,2]
#
# main procedure
#positions = sample(DEF_POSITIONS,5)
#squs = square_builder(positions)
#
#
#
#def square_builder(positions)
#    squares=[]
#    for pos in positions:
#        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
#        squ.setPos(pos)
#        squares.append(squ)
#    return squares
from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random


class SquarePos:
    def __init__(self, position, color):
        self.position = position
        self.color = color

def positions_builder():
    #pass
    return positions_array

def draw_square(squarePoss):
    for i, pos in enumerate(squarePoss):
        squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
        squ.setFillColor(pos.color)
        squ.setPos(pos.position)
        squ.draw()

def draw_circle(positions):
    for i, pos in enumerate(positions):
        cir =  visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        cir.setPos(pos)
        cir.draw()

def draw_dimond(positions):
    for i, pos in enumerate(positions):
        dim =  visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        dim.setPos(pos)
        dim.draw()


def draw_by_case(situation, squares_pos, draw_border_pos):
    if(situation==1):
        drawA(squares_pos, draw_border_pos)
    elif(situation==2):
        drawB(squares_pos, draw_border_pos)


def drawA(squares_pos, draw_border_pos):
    draw_square(squares_pos)
    draw_circle(draw_border_pos)
    WIN.flip()

def drawB(squares_pos, draw_border_pos):
    draw_square(squares_pos)
    draw_circle(draw_border_pos)
    draw_dimond(draw_border_pos)
    WIN.flip()

def request_answer():
    return answer

def log(situation, stoptime, positions, positions_a, positions_b, user_answer):
    return 1


def run(squares_pos):
    draw_border_pos = sample(POSITIONS, 4)
    not_draw_border_pos = list(set(squares_pos)-set(draw_border_pos))
    stoptime = random.uniform(.3, 2.0)
    situation = sample(CASES,1)[0]
    draw_by_case(situation, squares_pos, draw_border_pos)
    
    
    core.wait(stoptime)
    # user_answer = request_answer()
    # log(situation, stoptime, squares_pos, draw_border_pos, not_draw_border_pos, user_answer)
    return 1


CASES = [1,2]
WIN = visual.Window((800, 600), color="grey", units="pix")
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
COLORS = ['white', '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'blue']

squares_pos = []
colors = []

for i, pos in enumerate(POSITIONS):
    color = sample(COLORS, 1)[0];
    squ = SquarePos(pos, color)
    squares_pos.append(squ)
    colors.append(color)



for i in range(random.randint(1,10)):
    run(squares_pos)
