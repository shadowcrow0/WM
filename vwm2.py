from psychopy import visual, core, gui, event, data
from random import sample
from itertools import product, chain,  islice
import csv
import  setstim
FEEDBACK = []

expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}
# dlg = gui.DlgFromDict(dictionary=expInfo, title='VWM Task', order=['ID', 'age', 'block'])
# if dlg.OK:
#    toFile('lastParams.pickle', expInfo)  # save params to file for next time
# else:
#    core.quit()  # the user hit "cancel" so exit
WIN = visual.Window((1366, 800), color="grey", units="pix", fullscr=False)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',
                            color='white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(
    WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
phase = visual.TextStim(win=WIN, text='Practice block.\nPress the "Space" key to continue.', pos=(0, 6), height=0.8)
instr = visual.TextStim(win=WIN,text='Remmber position and color,\nif color belong same frame, press "Left",otherwise color belong diifent frame, press"Right".\n Press "space" to continue.', pos=(0, 4), height=0.8)
practice = visual.TextStim(win=WIN,text='This is the practice block.\n''Make judgment if color appear belong same frame.Press "Left",/n color appears in different frame, please press "Right".''Now press the "Space" key to start practice block.', pos=(0, -2), height=0.8)
col_new = []
COLORS = [(0, 230, 115),(255, 128, 0), (128, 0, 128), (0, 100, 0), (139, 69, 19) ,(255, 182, 193), (222, 184, 135), (255, 140, 0), (0, 102, 102), (107, 142, 35) ,(0, 128, 128)]


def drawStimulus(color, pos, downs, ups, cue_order, sz):
    drawLearningColors(color, pos)
    drawLearningCues(downs, ups, cue_order, sz)

def drawLearningColors(color, pos):
    squares = []
    print repr(int(color))
    for i in range(len(pos)):
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None,fillColorSpace='rgb255')
        squares.append(squ)
    for idx, squ in enumerate(squares):
        squ.setFillColor(color[idx],'rgb255')
        squ.setPos(pos[idx])
        squ.draw()
def drawLearningCues(downs, ups, sz, cue_order):  # make frame need seperately $ Lin: Failed to comprehence.
    if cue_order == 0:
        drawDiamondCue(downs, sz)
        drawCircleCue(ups, sz)
    else:
        drawDiamondCue(ups,sz)
        drawCircleCue(downs,sz)

def drawDiamondCue(positions, sz):
    diam = []
    for j in range(sz):
        dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
        diam.append(dim)
    for idx, dim in enumerate(diam):
        dim.setPos(positions[idx])
        dim.draw()

def drawCircleCue(positions, sz):
    circle = []
    for j in range(sz):
        cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
        circle.append(cir)
    for idx, cir in enumerate(circle):
        cir.setPos(pos2[idx])
        cir.draw()

def getProbeColor(col_new, cue, ProbeType, col_a, col_b):
    global col_positive, col_intrusion, display_color
    res = ProbeType
    if cue == 1:  # diamond circle
        col_positive = col_b
        col_intrusion = col_a
    elif cue == 0:  # circle diamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive[0]
    elif res == 1:
        display_color = col_intrusion[0]
    elif res == 2:
        display_color = sample(color_new,1)[0]
    return display_color

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
def drawProbe(ProbeType, col_a, col_b, cue, col_new):
    squ = visual.Rect(WIN, size=[100, 100], lineColor=None, pos=[
                      0, 0],fillColorSpace='rgb255')
    squ.setFillColor(display_color,'rgb255')
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
        FEEDBACK.append('p')
    return FEEDBACK
def save_resp(ans, rt, display_color, ProbeType, CSI, FEEDBACK, thisIndex, sz):
    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']+'_'+INFO['block']), 'a')
    dataFile.write(ans + ','+ rt +',' +display_color +','+ ProbeType +','+ CSI +','+ FEEDBACK +',' +thisIndex +','+ sz+'\n')
#######################################end of component######################


def showInstr():  # show instruction on screen
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    WIN.flip()

def learningPhase(color, pos, downs, ups, cue_order, sz):
    drawStimulus(color, pos, downs, ups, cue_order, sz)
    WIN.flip()

def recognitionPhase(CSI, ProbeType, col_a, col_b, cue, col_new):
    drawTestingCue(CSI, cue)
    display_color = getProbeColor(col_new, cue, ProbeType, col_a, col_b)
    (ans, rt) = drawProbe(ProbeType, col_a, col_b, cue, col_new)
    FEEDBACK = get_ans(ans, res= ProbeType)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    return  display_color, ans, rt, FEEDBACK

def testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, thisIndex, col_a, col_b,col_new,sz):
    (ans, rt, display_color, FEEDBACK) = recognitionPhase(CSI, ProbeType, col_a, col_b, cat1, col_new)
    save_resp(ans, rt, display_color, ProbeType, CSI, FEEDBACK, thisIndex, sz)
    (ans2, rt2, display_color2,FEEDBACK2) = recognitionPhase(CSI, ProbeType, col_a, col_b, cat2, col_new)
    save_resp(ans2, rt2, display_color2, ProbeType, CSI2, FEEDBACK2, thisIndex, sz)


# main function reacting to the response of the subject
def process(downs, ups, color, cue_order, CSI, ProbeType, ProbeType2, CSI2, col_a, col_b, pos, cat1, cat2, sz, thisIndex):
    col_new = list(set(COLORS) - set(color))
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    learningPhase(color, pos, downs, ups, cue_order, sz)
    core.wait(5)  # wait for 5000ms and erase them all
    testingPhase(CSI, cat1, ProbeType, CSI2, cat2, ProbeType2, color, col_a, col_b, col_new)

def main():
    round =80
    for i in range(round):
        process(sz = sz[i],downs = downs[i], ups = ups[i], color = color[i], cue_order = cue_order[i], CSI = CSIs[i], ProbeType = ProbeTypes[i], ProbeType2 = ProbeType2s[i], CSI2 = CSI2s[i], col_a = col_a[i], col_b = col_b[i], pos = pos[i], cat1 = cat1[i], cat2 = cat2[i],thisIndex = thisIndex[i])
main()