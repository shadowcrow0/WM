from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
import sys, time, random

#make class
class SquarePos:
    def __init__(self, position, color, category):
        self.posA = sample(POSITIONS,set_size)
        self.posB = list(set(POSITIONS) - set(posA))
        self.position = list(set(posB)+set(posA))
        self.color = list(set(catA_col)+set(catB_col))
        self.category = category #1 or 0
        self.newpos = [0,0]
        self.selected_colors = sample(COLORS, set_size*2)
        self.catA_col = selected_colors[:set_size+1] # 0
        self.catB_col = list(set(selected_colors) - set(catA_col)) #1
    def draw_cue(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 1)
            cir.setPos(self.posA)
            cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(135,135), ori =45, lineWidth =3 )
            dim.setPos(self.posB)
            dim.setFillColor('white')
            dim.draw()
    def draw_square(self, color=None):
        if color == None:
            color = self.color
        squ = visual.Rect(WIN, size=[100, 100],lineColor = 'white')
        squ.setFillColor(color)
        squ.setPos(self.position)
        squ.draw()
#make new def for reverse
    def set_cue(self, newpos,category):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 40, edges = 35, lineWidth = 1)
            cir.setPos(newpos)
            cir.setFillColor('white')
            cir.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(135,135), ori =45, lineWidth =3 )
            dim.setPos(self.newpos)
            dim.setFillColor('white')
            dim.draw()
    def show_res(self,newpos,selected_colors):
        squ = visual.Rect(WIN, size=[100, 100],lineColor = 'white')
        squ.setPos([0,0])
        squ.setFillColor(selected_colors)
        squ.draw()
#copy the function from old
#append ans to record[]
def save_ans(rt, ans, stoptime, res, situation,set_size,FEEDBACK):
    record = []
    record.append(rt, ans, stoptime, res, situation,set_size,FEEDBACK)
    print(rt, ans, stoptime, res, situation,set_size,FEEDBACK)
    print(record)

    return record

def get_setsize(n):
    count = [0]*4
    result = []
    for i in range(n):#n=160
        which_group = randint(0,3)
        count[which_group] += 1
        result.append(which_group+1)
    return result

def get_res(n):
    count = [0]*4 #for setsize=1 to setsize=4
    result = []
    for i in range(n):#n=160
        rand = randint(0,3) #randin(0,3) for 160 times
        while count[rand] == n/4:
            rand = randint(0,3)
        count[rand] += 1
        result.append(rand)# after count append result to the list
    for i in range(n):
        if result[i] == 3:
            result[i] = 0
    return result

def get_ans(ans,res):
    feedback = []
    for aws,resp in enumerate(ans,res):
        if ans == 's' and res ==1:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        elif ans =='k' and res ==2:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        elif ans == 'k' and res ==0:
            FEEDBACK_O.draw()
            FEEDBACK.append(1)
        else:
            FEEDBACK_X.draw()
            FEEDBACK.append(0)
    print(FEEDBACK)
    return FEEDBACK


def set_color(selected_colors):
    color_new = list(set(COLORS)- set(selected_colors))
    color_postive =[]
    color_intrusion =[]
    i = randint(0,1)
    j = randint(0,1)
    if i ==0 and j ==1: 
        color_postive.append(catA_col)
        color_intrusion.append(catB_col)
    elif j == 0 and i == 1:
        color_postive.append(catB_col)
        color_intrusion.append(catA_col)
    return color_intrusion, color_postive, color_new, selected_colors
 #feed the color

def run_stage1(squares_pos):
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    for cue in squares_pos:
        cue.draw_cue()
        cue.draw_square()
    WIN.flip()
    stoptime = 2
    core.wait(stoptime)

##########################need to double check#############
def run_cue(cue_list, stoptime, newpos,category):
    for cue in cue_list:
        cue.set_cue(newpos,category)
    WIN.flip()
    core.wait(stoptime)
#define category need to be present
#set position into [0,0]

def run_stage2(cue_list, selected_colors, res, color_new, color_intrusion, color_postive):
    target_cue= []
    if res == 0:
        display_color =color_new[0]#subject never seen before
    elif res == 1:
        display_color = color_postive[0]#belong same category
    else:
        display_color = color_intrusion[0] #belong different category
 #define display color
    for target_cue in res_pos:
    	target_cue.set_cue(newpos,category)
    	target_cue.show_res(newpos,selected_colors)
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['k', 's'])
    t2 = core.getTime()
    WIN.flip()
    return (ans, t2-t1) 

CASES = [0,1]
WIN = visual.Window((800, 600), color="grey", units="pix")
POSITIONS = [(100, 200), (100, -200), (-100, 200), (200, 100), (200, -100), (-200, 100), (-200, -100), (-100, -200)]
COLORS = [ '#0000FF', '#800080', '#FFC0CB','#FFFF00', '#1E90FF', '#008000', '#A52A2A','#F83759','#FFA500', '#C45366', '#7853C4', '#CFB46F', '#6FCF80']
STOPTIME_LIST = [ sample([0.3, 2],2) for x in range(120)]
RES_LIST = get_res(320)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=80, color='white', pos=(0, 0))
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'Practice':['Yes','No']}
gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age'])


def trial(stoptime, set_size, res):
    cue_category=[[],[]]
    squares_pos = []
    res_pos = []
    selected_colors = sample(COLORS, set_size*2)
    '''init'''
    for i, pos in enumerate(sample(POSITIONS, set_size*2)):
        color = selected_colors[i]
        category = randint(0,1)
        if len(cue_category[category]) == set_size: #A full or B full
            category = 0 if category == 1 else 1

        squ = SquarePos(pos, color, category)
        squares_pos.append(squ)
        cue_category[category].append(squ)

    run_stage1(squares_pos)
    WIN.flip()
    for i, situation in enumerate(sample(CASES, 2)):
        run_cue(cue_category[situation], stoptime[i],res_pos)
        WIN.flip()
        (ans, rt) = run_stage2(cue_category[situation], selected_colors, res)
        save_ans(rt=rt, ans=ans, stoptime=stoptime[i], res=res, situation=situation,set_size = set_size, FEEDBACK = FEEDBACK)


def main():
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 160
    setsize_list = get_setsize(rounds)
    for i in range(rounds):
        trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])

def practice():
    def demo():
        rounds = 4
        setsize_list = get_setsize(rounds)
        for i in range(rounds):
            trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    demo()
    end_demo = visual.TextStim(WIN, pos=(0, 4), height=30,
                            text='End of the demo, \nIt is your term now. Press "Space" to practice.', color = 'white')
    end_demo.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 12
    setsize_list = get_setsize(rounds)
    for i in range(rounds):
        trial(STOPTIME_LIST[i], setsize_list[i], RES_LIST[i])
