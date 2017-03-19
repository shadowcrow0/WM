from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random


class SquarePos:
    def __init__(self, position, color, category):
        self.position = position
        self.color = color
        self.category = category #1 or 2

    def draw_square(self, color=None):
        if color == None:
            color = self.color
        squ = visual.Rect(WIN, size=[115, 115],lineColor = 'grey')
        squ.setFillColor(color)
        squ.setPos(self.position)
        squ.draw()

    def draw_cue(self):
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        cir.setPos(self.position)
        cir.draw()
        if self.category == 2:
            dim = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
            dim.setPos(self.position)
            dim.draw()


def positions_builder():
    #pass
    return positions_array


def request_answer():
    return answer

def log(situation, stoptime, positions, positions_a, positions_b, user_answer):
    return 1

def save_ans(rt, ans, stoptime, res, situation):
    pass

def get_res(n):
    count = [0]*4
    result = []
    for i in range(n):#n=160
        rand = randint(4)
        while count[rand] == n/4:
            rand = randint(4)
        count[rand] += 1
        result.append(rand)
    for i in range(n):
        if result[i] == 3:
            result[i] = 0
    return result

def get_cue():
    num = len(squares_pos)
    temp_list = [ (x+1) for x in range(num)]
    A_cue = sample(squares_pos, int(num/2))
    B_cue = list(set(squares_pos)-set(A_cue))

    return (A_cue, B_cue)

def run_stage1():
    for cue in squares_pos:
        cue.draw_square()
        cue.draw_cue()

    WIN.flip()
    stoptime = 2
    core.wait(stoptime)

def run_cue(cue_list, stoptime):
    for cue in cue_list:
        cue.draw_cue()
    WIN.flip()
    core.wait(stoptime)

def run_stage2(cue_list, selected_colors, res):
    target_cue = sample(cue_list, 1)[0]

    if res == 0:
        display_color = sample(list(set(COLORS) - set(selected_colors)), 1)[0]
    elif res == 1:
        display_color = target_cue.color
    else:
        display_color = sample(selected_colors, 1)[0]

    target_cue.draw_square(display_color)
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['k', 's'])
    t2 = core.getTime()

    return (ans, t2-t1)





CASES = [0,1]
WIN = visual.Window((800, 600), color="grey", units="pix")
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
COLORS = [ '#FFDA00', '#52FFAE', '#3E0DE4','#F8E214', '#CDF118', '#A52A2A', '#1118BB','#6C3EFF','green', 'yellow', 'orange', 'cyan', 'purple', 'blue']
STOPTIME_LIST = [ sample([0.3, 2],2) for x in range(120)]
RES_LIST = get_res(160)

squares_pos = []
colors = []

def trial(stoptime, set_size, res):
    cue_category=[[]*2]
    selected_colors = sample(COLORS, set_size*2)

    '''init'''
    for i, pos in enumerate(sample(POSITIONS, set_size*2)):
        color = selected_colors[i]
        category = randint(2)
        if len(cue_category[category]) == set_size: #A full or B full
            category = 0 if category == 1 else 1

        squ = SquarePos(pos, color, category)
        squares_pos.append(squ)
        cue_category[category].append(squ)

    run_stage1()
    WIN.flip()
    situation = sample(CASES, 1)[0]
    run_cue(cue_category[situation], stoptime[0])
    WIN.flip()
    (ans, rt) = run_stage2(cue_category[situation], selected_colors, res)
    save_ans(rt=rt, ans=ans, stoptime=stoptime, res=res, situation=situation)

for i in range(160):
    trial(STOPTIME_LIST[i], int(i/40)+1, RES_LIST[i])

'''
for i in range(random.randint(1,10)):
    run(squares_pos)
'''
