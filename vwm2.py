from psychopy import visual, core, gui, event, data
from psychopy.tools.filetools import fromFile, toFile
from random import sample
from itertools import product, chain,  islice
import csv

#INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'block':''}
#gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age','block'])
WIN = visual.Window((1366, 800), color="grey", units="pix", fullscr=False)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',
                            color='white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
COLOR = [(0, 230, 115),
         (255, 128, 0),
         (128, 0, 128),
         (0, 100, 0),
         (139, 69, 19),
         (255, 182, 193),
         (222, 184, 135),
         (255, 140, 0),
         (0, 102, 102),
         (107, 142, 35),
         (0, 128, 128)]

p1 = (100, 200)
p2 = (-100, 200)
p3 = (-200, 100)
p4 = (200, 100)
p5 = (200, -100)
p6 = (100, -200)
p7 = (-200, -100)
p8 = (-100, -200)



phase = visual.TextStim(
    win=WIN, text='Practice block.\nPress the "Space" key to continue.',
    pos=(0, 6), height=0.8)
instr = visual.TextStim(
    win=WIN,
    text='Remmber position and color,\nif color belong same frame, press "Left",otherwise color belong diifent frame, press"Right".\n Press "space" to continue.',
    pos=(0, 4), height=0.8)
practice = visual.TextStim(
    win=WIN,
    text='This is the practice block.\n'
    'Make judgment if color appear belong same frame.Press "Left",/n color appears in different frame, please press "Right".'
    'Now press the "Space" key to start practice block.',
    pos=(0, -2), height=0.8)
###############value import by csv##########
sz = []  # setsize, determine how many squares need to present
ProbeType2 = []
CSI2 = []
ProbeType = []
CSI = []
cue = []
thisN = []
thisIndex = []
col_a = []  # col_a -> top 4 squares
color = []
col_b = []  # col_b -> down 4 squares
ups = []  # top 4 positions
pos = []  # all position
downs = []  # down 4 position
cat1 = []
cat2 = []
FEEDBACK = []


#    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']+'_'+INFO['block']), 'a')
#    #dataFile.write('rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK\n')
#    rt = str(rt)
#    ans=str(ans)
#    stoptime=str(stoptime)
#    res = str(res)
#    category = str(category)
#    setsize = str(setsize)
#    FEEDBACK= str(FEEDBACK)
#    display_color = str(display_color)
#    col_positive = str(col_positive)
#    col_intrusion = str(col_intrusion)
#    pos_squ = str(pos_squ)
#    pos_cir = str(pos_cir)
#    positions = str(positions)
#    rounds = str(rounds)
#    dataFile.write(rt+','+ ans+','+stoptime+','+res+','+ category+','+ setsize+','+ FEEDBACK+','+ display_color+','+col_positive+','+ cols_intrusion +','+ pos_squ+','+ pos_cir+','+ positions +','+ rounds+'\n')

col_a = [(0, 102, 102), (0, 230, 115)]
color = [(107, 142, 35), (0, 230, 115), (0, 102, 102), (222, 184, 135)]
col_b = [(0, 102, 102), (222, 184, 135)]
ups = [(200, 100), (-100, 200)]
pos = [(200, 100), (-100, 200), (-200, -100), (100, -200)]
downs = [(-200, -100), (100, -200)]
COLORS = [(0, 230, 115), (255, 128, 0), (128, 0, 128), (0, 100, 0), (139, 69, 19), (255,
                                                                                    182, 193), (222, 184, 135), (255, 140, 0), (0, 102, 102), (107, 142, 35), (0, 128, 128)]

sz = 4
cue = 1
CSI = .3
ProbeType = 0
ProbeType2 = 2
CSI2 = 5
cat1 = 0
cat2 = 1


def square(color, pos):
    squares = []
    for i in range(len(pos)):
        squ = visual.Rect(WIN, fillColorSpace="rgb255",
                          size=[100, 100], lineColor=None)
        squares.append(squ)
    # 8. draw squares with color.
    for idx, squ in enumerate(squares):
        squ.setFillColor(color[idx],'rgb255')
        squ.setPos(pos[idx])
        squ.draw()


def determine_cue(cat):
    if cat == 0:
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        cir.setPos([0, 0])
        cir.draw()
    elif cat == 1:
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        dim.setPos([0, 0])
        dim.draw()


def chose_pos(downs, ups, cue):  # make frame need seperately
    if cue == 0:
        cir_dim(ups, downs)
    elif cue == 1:
        dim_cir(ups, downs)


def set_cols(COLORS, color, cat1, ProbeType, col_a, col_b):
    col_new = list(chain.from_iterable(set(COLORS) - set(color)))
    cue = cat1
    res = ProbeType
    if cue == 1:  # diamond circle
        col_positive = col_b
        col_intrusion = col_a
    elif cue == 0:  # circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive[0]
    elif res == 1:
        display_color = col_intrusion[0]
    elif res == 2:
        display_color = col_new[0]
    return display_color
# about cue and position
# if cue = 0 refer ups fill with circle, and downs fill in diamond
# if cue = 1 refer ups -> diamond, downs -> circle


def set_cols2(COLORS, color, cat2, ProbeType2, col_a, col_b):
    col_new = list(chain.from_iterable(set(COLORS) - set(color)))
    cue = cat2
    res = ProbeType2
    if cue == 1:  # diamond circle
        col_positive = col_b
        col_intrusion = col_a
    elif cue == 0:  # circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive[0]
    elif res == 1:
        display_color = col_intrusion[0]
    elif res == 2:
        display_color = col_new[0]
    return display_color


def dim(pos1):
    diam = []
    for j in range(len(pos1)):
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        diam.append(dim)
    for idx, dim in enumerate(diam):
        dim.setPos(pos1[idx])
        dim.draw()


def cir(pos2):
    circle = []
    for j in range(len(pos2)):
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        circle.append(cir)
    for idx, cir in enumerate(circle):
        cir.setPos(pos2[idx])
        cir.draw()


def cir_dim(ups, downs):
    dim(pos1=downs)
    cir(pos2=ups)


def dim_cir(ups, downs):
    dim(pos1=ups)
    cir(pos2=downs)


def cue1(CSI, cat1):
    cat = cat1
    determine_cue(cat)
    WIN.flip()
    core.wait(CSI)


def cue2(CSI2, cat2):
    cat = cat2
    determine_cue(cat)
    WIN.flip()
    core.wait(CSI2)


def probe1(ProbeType, COLORS, color, col_a, col_b, cat1):
    display_color = set_cols(COLORS, color, cat1, ProbeType, col_a, col_b)
    squ = visual.Rect(WIN, size=[100, 100], lineColor=None, pos=[
                      0, 0], fillColorSpace="rgb255")
    squ.setFillColor(display_color)
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2 - t1)


def probe2(ProbeType2, COLORS, color, col_a, col_b, cat2):
    display_color = set_cols2(COLORS, color, cat2, ProbeType2, col_a, col_b)
    squ = visual.Rect(WIN, size=[100, 100], lineColor=None, pos=[
                      0, 0], fillColorSpace="rgb255")
    squ.setFillColor(display_color)
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2 - t1)


def get_ans(ans, res):
    if res == 0 and ans == ['left']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 1 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 2 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res == 0 and ans == ['right']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res == 1 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res == 2 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif ans == ['left''right'] and ans == ['right''left']:
        FEEDBACK.append(p)
    return FEEDBACK


#######################################end of component######################


def showInstr():  # show instruction on screen
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    WIN.flip()


# main function reacting to the response of the subject
def process(downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, thisIndex):
    square(color, pos)
    chose_pos(downs, ups, cue)
    WIN.flip()
    core.wait(5)  # wait for 5000ms and erase them all
    cue1(CSI, cat1)
    (ans, rt) = probe1(ProbeType, COLORS, color, col_a, col_b, cat1)
    get_ans(ans, res=ProbeType)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    cue2(CSI2, cat2)
    (ans2, rt2) = probe2(ProbeType2, COLORS, color, col_a, col_b, cat2)
    get_ans(ans, res=ProbeType2)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    print thisIndex

