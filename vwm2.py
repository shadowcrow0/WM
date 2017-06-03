from psychopy import visual, core, gui, event, data
from psychopy.tools.filetools import fromFile, toFile
from random import sample
from itertools import product, chain,  islice
import csv
global display_color
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

col_a = ['#006666','#00e673']
color = ['#ff8000', '#800080','#006666','#00e673']
col_b = ['#ff8000', '#800080']
ups = [(200, 100), (-100, 200)]
pos = [(200, 100), (-100, 200), (-200, -100), (100, -200)]
downs = [(-200, -100), (100, -200)]
COLORS =['#00E673','#ff8000', '#800080','#006400' ,'#8b4513' ,'#ffb6c1', '#deb887', '#ff8c00','#006666','#6b8e23' ,'#008080']
new = list(set(COLORS) - set(color))
col_new = new[0]
sz = 4
cue_order = 1
CSI =.3
ProbeType =0
ProbeType2 =2
CSI2 = 5
cat1 = 0
cat2 = 1
new = list(set(COLORS) - set(color))
col_new = new[0]

def drawStimulus(color, pos, downs, ups, cue_order):
    drawLearningColors(color, pos)
    drawLearningCues(downs, ups, cue_order)

def drawLearningColors(color, pos):
    squares = []
    for i in range(len(pos)):
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None)
        squares.append(squ)
    for idx, squ in enumerate(squares):
        squ.setFillColor(color[idx])
        squ.setPos(pos[idx])
        squ.draw()
def drawLearningCues(downs, ups, cue_order):  # make frame need seperately $ Lin: Failed to comprehence.
    if cue_order == 0:
        drawDiamondCue(positions = downs)
        drawCircleCue(positions = ups)
    else:
        drawDiamondCue(positions = ups)
        drawCircleCue(positions = downs)

def drawDiamondCue(positions):
    diam = []
    for j in range(len(positions)):
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        diam.append(dim)
    for idx, dim in enumerate(diam):
        dim.setPos(positions[idx])
        dim.draw()

def drawCircleCue(positions):
    circle = []
    for j in range(len(positions)):
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        circle.append(cir)
    for idx, cir in enumerate(circle):
        cir.setPos(positions[idx])
        cir.draw()



def drawTestingCue(CSI, cue):
    if cue == 0:
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        cir.setPos([0, 0])
        cir.draw()
    elif cue == 1:
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        dim.setPos([0, 0])
        dim.draw()
    WIN.flip()
    core.wait(CSI)

def determinedisplaycolor(ProbeType, col_new, col_a, col_b, cue):
    display_color = []
    res = ProbeType
####define cue_order
    if cue == 1 and res ==0:  # diamond circle
        col_positive = col_b[0]
        display_color = col_positive
    elif cue == 1 and res ==1:  # diamond circle
        col_intrusion = col_a[0]
        display_color = col_intrusion
    elif cue == 1 and res ==2:  # diamond circle
        display_color =  col_new[0]
    if cue == 0 and res ==0:  # diamond circle
        col_positive = col_a[0]
        display_color = col_positive
    elif cue == 0 and res ==1:  # diamond circle
        col_intrusion = col_b[0]
        display_color = col_intrusion
    elif cue == 0 and res ==2:  # diamond circle
        display_color =  col_new[0]
    return display_color
def drawProbe(display_color):
    squ = visual.Rect(WIN, size=[100, 100], lineColor=None,pos=[0, 0])
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

def learningPhase(color, pos, downs, ups, cue_order):
    drawStimulus(color, pos, downs, ups, cue_order)
    WIN.flip()
    core.wait(5)

def recognitionPhase(CSI, cat1, ProbeType, col_a, col_b, col_new):
    drawTestingCue(CSI, cat1)
    display_color = determinedisplaycolor(ProbeType, col_new, col_a, col_b, cue)
    (ans, rt) = drawProbe(display_color)
    get_ans(ans, res=ProbeType)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    return ans
learningPhase(color, pos, downs, ups, cue_order)
recognitionPhase(CSI, cat1, ProbeType, col_a, col_b, col_new)
def testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, color, col_a, col_b,COLORS):
    ans = recognitionPhase(CSI, cat1, ProbeType, color, col_a, col_b, COLORS)
    ans = recognitionPhase(CSI2, cat2, ProbeType2, color, col_a, col_b, COLORS)

# main function reacting to the response of the subject
def process(downs, ups, color, cue_order, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, thisIndex, COLORS):
    learningPhase(color, pos, downs, ups, cue_order)
    core.wait(5)  # wait for 5000ms and erase them all

    testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, color, col_a, col_b, COLORS)
    print thisIndex
process(downs, ups, color, cue_order, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, thisIndex, COLORS)
