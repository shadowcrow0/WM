from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random
from itertools import chain


class SquarePos:
    def __init__(self, position, color, category):
        self.position = position
        self.color = color
        self.category = category #1 or 0
    def draw_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 4)
            cir.setPos(self.position)
            #cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(150,150), ori =45, lineWidth =4)
            dim.setPos(self.position)
            #dim.setFillColor('white')
            dim.draw()

    def draw_square(self, color=None):
        if color == None:
            color = self.color
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(color)
        squ.setPos(self.position)
        squ.draw()
    def determine_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 4)
            cir.setPos([0,0])
#            cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(150,150), ori =45, lineWidth =4)
            dim.setPos([0,0])
 #           dim.setFillColor('white')
            dim.draw()
    def draw_res(self,display_color):
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(display_color)
        squ.setPos([0,0])
        squ.draw()




def save_ans(rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK):
    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']), 'a')
    dataFile.write(str(rt) +', '+str(ans)+', '+ str(stoptime) +','+ str(res)+ ','+ str(situation) +','+str(SET_SIZE)+','+str(FEEDBACK)+'\n')




def get_res(n):
    count = [0]*4
    result = []
    for i in range(n):#n=160
        rand = randint(0,3)
        while count[rand] == n/4:
            rand = randint(0,3)
        count[rand] += 1
        result.append(rand)
    for i in range(n):
        if result[i] == 3:
            result[i] = 0
    return result

def get_setsize(n):
    result =[]
    for i in range(n):
        k = [1,2,3,4]
        l= sample(k,4)
        result.append(l)
    result =list(chain.from_iterable(result))
    return result


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


def run_stage2(cue_list, selected_colors, res,cat_col,color_new):
    target_cue = sample(cue_list, 1)[0]
    category= target_cue.category #targetcue's attribute
    color_postive = cat_col[category]
    negative = 0 if category == 1 else 1 #inline if
    color_intrusion =cat_col[negative]
    if res == 0:
        display_color = sample(color_postive,1)[0]
    elif res == 1: 
        display_color = sample(color_new,1)[0]
    elif res ==2:
        display_color = sample(color_intrusion, 1)[0]
    target_cue.determine_cue()
    target_cue.draw_res(display_color)
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['k', 's'])
    t2 = core.getTime()
    get_ans(ans, res)
    WIN.flip()
    core.wait(1)
    return (ans, t2-t1)


def get_ans(ans,res):
    FEEDBACK =[]
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
    return FEEDBACK

INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female']}
gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age'])
CASES = [0,1]
WIN = visual.Window((1366, 800), color="grey", units="pix",fullscr = True)
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
COLORS = [ '#0000FF', '#800080', '#FFC0CB','#FFFF00', '#1E90FF', '#008000', '#A52A2A','#F83759','#FFA500', '#C45366', '#7853C4', '#CFB46F', '#6FCF80']
STOPTIME_LIST = [ sample([0.3, 2],2) for x in range(160)]
RES_LIST = get_res(8)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=80, color='white', pos=(0, 0))
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FEEDBACK_O = visual.TextStim(WIN, pos=(0, 4), height=30,text='Correct.', color = 'white')
FEEDBACK_X = visual.TextStim(WIN, pos=(0, 4), height=30,text='Wrong.', color = 'white')
SET_SIZE = 0
FEEDBACK =[]


def trial(stoptime, res):

    cue_category=[[],[]]
    selected_colors = sample(COLORS, SET_SIZE*2)
    color_new = list(set(COLORS)- set(selected_colors))
    squares_pos = []
    cat_col = [[],[]]
    '''init'''

    for i, pos in enumerate(sample(POSITIONS, SET_SIZE*2)):
        color = selected_colors[i]
        category = randint(0,1)
        if len(cue_category[category]) == SET_SIZE: #A full or B full
            category = 0 if category == 1 else 1
        cat_col[category].append(color)
        squ = SquarePos(pos, color, category)
        squares_pos.append(squ)
        cue_category[category].append(squ)

    run_stage1(squares_pos)
    for i, situation in enumerate(sample(CASES, 2)):
        run_cue(cue_category[situation], stoptime[i])
        WIN.flip()
        (ans, rt) = run_stage2(cue_category[situation], selected_colors, res,cat_col,color_new)
        WIN.flip()
    save_ans(rt=rt, ans=ans, stoptime=stoptime[i], res=res, situation=situation,SET_SIZE = SET_SIZE, FEEDBACK= FEEDBACK)



def main():
    global SET_SIZE
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 1
    setsize_list = get_setsize(rounds)
    print(setsize_list)
    print(RES_LIST)
    for i in range(rounds):
        SET_SIZE= setsize_list[i]
        trial(STOPTIME_LIST[i], RES_LIST[i])

main()
