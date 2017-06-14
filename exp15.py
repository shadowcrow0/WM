from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random
from itertools import chain
class SquarePos:
    def __init__(self, position_neg, position_pos ,color, category):
        self.position_pos = position_pos
        self.position_neg = position_neg
        self.position= position
        self.color = color
        self.category = category #1 or 0
    def draw_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos(self.position_pos)
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos(self.position_neg)
            dim.draw()
    def draw_square(self, color=None):
        if color == None:
            color = self.color
        squ = visual.TextStim(WIN,height=60)
        squ.setText(color)
        squ.setPos(self.position)
        squ.draw()
    def determine_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos([0,0])
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos([0,0])
            dim.draw()
    def draw_res(self,display_color):
        squ = visual.TextStim(WIN, color = 'white',height =60)
        squ.setText(display_color)
        squ.setPos([0,0])
        squ.draw()

def save_ans(rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK, selected_colors, selected_pos,cols_intrusion,cols_positive):
    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']+'_'+INFO['block']), 'a')
    #dataFile.write('rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK\n')
    rt = str(rt)
    ans = str(ans)
    stoptime = str(stoptime)
    res = str(res)
    situation = str(situation)
    SET_SIZE = str(SET_SIZE)
    FEEDBACK = str(FEEDBACK)
    selected_colors = str(selected_colors) 
    selected_pos = str(selected_pos)
    cols_intrusion = str(cols_intrusion)
    cols_positive = str(cols_positive)
    dataFile.write(rt+','+ans+','+stoptime+','+res+','+situation+','+SET_SIZE+','+FEEDBACK+','+selected_colors+','+selected_pos+','+cols_intrusion+','+cols_positive+'\n')
#    ,'+cols_intrusion+','+cols_positive+'\n')



def get_setsize(n):
    result =[]
    for i in range(n):
        k = [1,2,3,4]
        l= sample(k,4)
        result.append(l)
    r =list(chain.from_iterable(result))
    return r


def run_stage1(squares_pos):
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    for cue in squares_pos:
        cue.draw_cue()
        cue.draw_square()
    WIN.flip()
    core.wait(2)


def run_cue(cue_list, stoptime):
    for cue in cue_list:
        cue.determine_cue()
    WIN.flip()
    core.wait(stoptime)
 
def run_stage2(cue_list, selected_colors,cat_col,color_new):
    target_cue = sample(cue_list, 1)[0]
    category= target_cue.category #targetcue's attribute
    color_postive = cat_col[category]
    negative = 0 if category == 1 else 1 #inline if
    color_intrusion =cat_col[negative]
    cols_positive = sample(color_postive,1)[0]
    cols_intrusion = sample(color_intrusion,1)[0]
    if cols_intrusion == cols_positive:
        cols_intrusion = sample(color_intrusion,1)[0]
    y = sample([2,1,0,0],1)
    res = y[0]
    #print y
    if res == 0: 
        display_color = cols_positive
    elif res == 1: #positive
        display_color = sample(color_new,1)[0]
    elif res ==2:
        display_color = cols_intrusion
    target_cue.draw_res(display_color)
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['k', 's'])
    t2 = core.getTime()
    return (ans, t2-t1,res,cols_intrusion,cols_positive)

def get_ans(ans,res):
    if res ==0 and ans == ['s']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==1 and ans ==['k']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==2 and ans ==['k']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==0 and ans ==['k']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==1 and ans ==['s']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==2 and ans ==['s']:
        FEEDBACK_X.draw() 
        FEEDBACK.append(0)
    elif ans ==['s''k'] and ans == ['k''s']:
        FEEDBACK.append(p)
    return FEEDBACK

INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'block':''}
gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age','block'])
CASES = [0,1]
WIN = visual.Window((1366, 800), color="grey", units="pix",fullscr = True)
POSITIONS_pos = [(100, 200), (-100, 200), (200, 100),  (-200, 100)]
POSITIONS_neg = [(100, -200), (200, -100),  (-200, -100), (-100, -200)]

COLORS = ['I','II','III','IV','V','VI','VII','VIII', 'IX', 'XI','XII', 'X']

STOPTIME_LIST = [ sample([0.3, 2],2) for x in range(480)]
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember word and frame, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(WIN, pos=(0, 4), height=30,text='Correct.', color = 'white')
FEEDBACK_X = visual.TextStim(WIN, pos=(0, 4), height=30,text='Wrong.', color = 'white')
FEEDBACK = []
SET_SIZE = 0
RECORD = []
RES_LIST = [2, 0, 1, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 2, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 1, 0, 1, 2, 0, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 0, 1, 2, 1, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 0, 1, 0, 2, 0, 0, 2, 1, 0, 0, 1, 2, 2, 0, 0, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 0, 2, 1, 0, 0, 0, 2, 1, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 2, 0, 0, 2, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 2, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 2, 0, 1, 0, 2, 0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 2, 0, 0, 2, 0, 1, 0, 1, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 1, 2, 0, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 2, 0, 2, 0, 1, 1, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 0, 2, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 0, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 2, 0, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 0, 2, 0, 1, 2, 0, 0, 1, 1, 0, 0, 2, 0, 1, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 2, 0, 0, 2, 0, 1, 2, 0, 0, 1, 2, 1, 0, 0, 0, 1, 2, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 1, 2, 1, 0, 0, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 1, 2, 2, 0, 1, 0, 2, 0, 0, 1, 0, 0, 1, 2, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 0, 2, 0, 1, 2, 0, 0, 0, 1, 2, 1, 0, 0, 2, 1, 0, 0, 2, 0, 1, 2, 0, 2, 0, 0, 1, 1, 0, 2, 0, 0, 1, 2, 0, 1, 0, 0, 2, 0, 0, 1, 2, 2, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1, 2, 2, 0, 1, 0, 0, 1, 0, 2, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2, 0, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 0, 0, 2, 1, 2, 0, 1, 0, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 2, 0, 0, 1, 0, 1, 2, 0, 1, 0, 0, 2, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 1, 2, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 2, 1, 0, 2, 1, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 0, 1, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 2, 0, 1, 2, 0, 0, 1, 2, 0, 0, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 0, 2, 0, 1, 1, 0, 0, 2, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 2, 0, 0, 1, 2, 0, 0, 1, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 2, 0, 1, 1, 2, 0, 0, 0, 1, 2, 0, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 0, 1, 1, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 2, 1, 0, 1, 0, 0, 2, 0, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 0, 2, 1, 0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 2, 0, 1, 0, 1, 2, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 1, 0, 0, 2, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 1, 2, 1, 0, 2, 0, 0, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0, 0, 0, 0, 2, 1, 2, 0, 0, 1, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 1, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 0, 2, 0, 1, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 0, 2, 1, 0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 2, 1, 2, 0, 1, 0, 2, 0, 0, 1, 0, 1, 2, 0, 2, 0, 1, 0, 1, 0, 0, 2, 0, 1, 2, 0, 2, 0, 0, 1, 0, 2, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 1, 2, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 0, 2, 0, 1, 0, 2, 0, 1, 1, 2, 0, 0, 1, 0, 2, 0, 1, 0, 0, 2, 2, 0, 1, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 2, 0, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2, 1, 0, 2, 0, 1, 0, 2, 0, 0, 0, 1, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 2, 0, 2, 0, 0, 1, 0, 1, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 0, 2, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 1, 0, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 2, 1, 2, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 1, 1, 0, 2, 0, 1, 2, 0, 0, 1, 0, 0, 2, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 1, 2, 1, 0, 0, 2, 0, 2, 1, 0, 0, 1, 2, 0, 0, 2, 0, 1, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 0, 2, 0, 2, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 0, 0, 2, 1, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 1, 0, 0, 2, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1, 0, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 1, 0, 2, 2, 1, 0, 0, 2, 1, 0, 0, 0, 1, 2, 0, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 1, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 2, 2, 0, 0, 1, 1, 2, 0, 0, 0, 0, 2, 1, 0, 2, 1, 0, 0, 2, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 0, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0, 2, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 0, 1, 2, 0, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1, 0, 1, 2, 0, 0, 0, 0, 2, 1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 0, 2, 0, 1, 0, 1, 2, 0, 2, 0, 1, 0, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 1, 0, 2, 0, 0, 1, 2, 0, 0, 0, 2, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 0, 2, 0, 0, 1, 0, 2, 2, 1, 0, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 2, 1, 2, 0, 0, 1, 2, 0, 1, 0, 1, 0, 0, 2, 0, 1, 2, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 0, 2, 1, 0, 2, 0, 0, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 2, 1, 0, 0, 1, 0, 0, 2, 0, 1, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 0, 1, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 1, 0, 2, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 0, 2, 0, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 2, 1, 2, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 1, 0, 0, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 0, 0, 1, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 0, 2, 1, 0, 2, 0, 2, 0, 0, 1, 1, 0, 2, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 1, 2, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 1, 0, 2, 2, 0, 0, 1, 1, 0, 2, 0, 1, 0, 0, 2, 2, 0, 1, 0, 0, 1, 0, 2, 1, 0, 2, 0, 0, 1, 2, 0, 1, 0, 0, 2, 0, 0, 2, 1, 1, 2, 0, 0, 0, 1, 2, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 1, 0, 2, 1, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 2, 1, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 0, 2, 1, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 2, 0, 1, 0, 0, 1, 2, 1, 0, 2, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 1, 0, 1, 2, 0, 0, 1, 0, 0, 2, 0, 2, 1, 0, 0, 1, 0, 2, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 0, 0, 0, 2, 1, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 1, 2, 1, 0, 0, 2, 0, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 1, 2, 0, 1, 0, 0, 2, 2, 1, 0, 0, 0, 0, 2, 1, 2, 1, 0, 0, 0, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 1, 2, 0, 2, 0, 0, 1, 2, 0, 1, 0, 0, 1, 0, 2, 1, 2, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 0, 1, 2, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 0, 2, 0, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 2, 1, 0, 2, 0, 1, 2, 0, 0, 1, 0, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 1, 2, 0, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 2, 0, 0, 2, 0, 1, 0, 0, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 0, 1, 2, 0, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 1, 0, 2, 0, 1, 2, 1, 0, 0, 0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1, 0, 2, 0, 1, 2, 0, 2, 1, 0, 0, 1, 0, 0, 2, 0, 0, 2, 1, 1, 0, 2, 0, 1, 2, 0, 0, 0, 2, 0, 1, 2, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 2, 0, 1, 1, 0, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 2, 2, 0, 1, 0, 0, 2, 0, 1, 0, 2, 1, 0, 1, 0, 0, 2, 0, 2, 1, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 1, 2, 0, 2, 1, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 2, 1, 0, 2, 0, 0, 1, 2, 1, 0, 0, 2, 0, 1, 0, 0, 0, 2, 1, 0, 0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 0, 0, 2, 1, 0, 1, 0, 2, 0, 2, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1, 1, 2, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 0, 2, 0, 1, 0, 1, 0, 2, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2, 1, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 2, 0, 0, 2, 0, 1, 1, 2, 0, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 0, 1, 2, 0, 0, 2, 1, 1, 0, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 2, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1, 2, 0, 0, 1, 1, 0, 2, 0, 0, 1, 0, 2, 0, 1, 0, 2, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 2, 0, 2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 2, 1, 0, 1, 0, 2, 0, 1, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 1, 2, 0, 0, 1, 0, 2, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 2, 0, 0, 1, 2, 0, 1, 0, 2, 0, 2, 1, 0, 0, 0, 0, 2, 1, 1, 0, 0, 2, 0, 1, 2, 0, 0, 0, 1, 2, 2, 0, 1, 0, 0, 1, 0, 2, 2, 1, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 1, 0, 2, 1, 0, 0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 0, 0, 2, 1, 0, 2, 0, 1, 2, 0, 0, 1, 1, 2, 0, 0, 2, 1, 0, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 2, 2, 1, 0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 0, 1, 0, 2, 1, 0, 0, 2, 1, 2, 0, 0, 0, 0, 2, 1, 1, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 0, 0, 2, 0, 1, 0, 0, 2, 1, 1, 2, 0, 0, 0, 1, 2, 0, 1, 0, 0, 2, 0, 0, 2, 1, 1, 2, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 0, 1, 2, 0, 2, 0, 1, 0, 0, 0, 1, 2, 0, 2, 0, 1, 2, 0, 1, 0, 0, 0, 2, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 0, 2, 1, 1, 0, 0, 2, 0, 0, 2, 1, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 2, 1, 2, 1, 0, 0, 1, 0, 0, 2, 1, 2, 0, 0, 2, 1, 0, 0, 1, 0, 2, 0, 0, 0, 2, 1, 0, 1, 2, 0, 2, 0, 0, 1, 0, 0, 2, 1, 2, 1, 0, 0, 2, 0, 1, 0, 0, 1, 2, 0, 1, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2, 1, 2, 0, 0, 1, 0, 0, 2, 0, 2, 0, 1, 0, 0, 2, 1, 1, 0, 2, 0, 1, 0, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 0, 0, 1, 2, 2, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2, 1, 0, 0, 2, 1, 0, 2, 0, 1, 0, 1, 0, 2, 1, 0, 0, 2, 0, 1, 0, 2, 0, 1, 2, 0, 1, 0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 0, 1, 0, 2, 0, 0, 0, 1, 2, 0, 2, 0, 1, 1, 0, 0, 2, 0, 2, 1, 0, 0, 2, 1, 0]
REST_MSG = visual.TextStim(WIN, pos=(0, 4), height=50,
                            text='Just finished block, please take a rest,\nPress "Space" to continue.', color = 'white')
def trial(stoptime):
    cue_category=[[],[]]
    selected_colors = sample(COLORS, SET_SIZE*2)
    selected_pos_pos =sample(POSITIONS_pos, SET_SIZE)
    selected_pos_neg =sample(POSITIONS_neg, SET_SIZE)
    selected_pos = list(chain.from_iterable(selected_pos_pos + selected_pos_neg))
    color_new = list(set(COLORS)- set(selected_colors))
    squares_pos = []
    cat_col = [[],[]]
    '''init'''
    for i, pos in enumerate(selected_pos):
        color = selected_colors[i]
        category = randint(0,1)
        if len(cue_category[category]) == SET_SIZE: #A full or B full
            category = 0 if category == 1 else 1
        cat_col[category].append(color)
        position_neg = selected_pos_neg
        position_pos = selected_pos_pos 
        squ = SquarePos(color, category, pos)
        squares_pos.append(squ)
        cue_category[category].append(squ)

    run_stage1(squares_pos)
    for i, situation in enumerate(sample(CASES, 2)):
        t0 = run_cue(cue_category[situation], stoptime[i])
        WIN.flip()
        (ans,rt,res,cols_intrusion,cols_positive) = run_stage2(cue_category[situation], selected_colors, cat_col,color_new)
        WIN.flip()
        get_ans(ans,res)
        WIN.flip()
        core.wait(.8)
        save_ans(rt = rt,ans=ans, stoptime=stoptime[i], res = res, situation=situation,SET_SIZE = SET_SIZE, FEEDBACK= FEEDBACK,selected_colors= selected_colors,selected_pos= selected_pos, cols_intrusion = cols_intrusion,cols_positive=cols_positive)
        FEEDBACK.pop()

#,color_new=color_new,cat_col=cat_col,selected_pos =selected_pos


def main():
    global SET_SIZE
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 80
    res= RES_LIST
    setsize_list = get_setsize(rounds)
    for i in range(rounds):
        SET_SIZE= setsize_list[i]
        trial(STOPTIME_LIST[i])

main()
