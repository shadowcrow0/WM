from itertools import product, chain,  islice
from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
FEEDBACK = []
CASES = [0,1]
SZ_LIST = [sample([1,2,3,4],4) for x in range(12)]
WIN = visual.Window((1024, 768), monitor='testMonitor',color="grey", units="pix", fullscr=False)
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title='VWM Task', order=['ID', 'age', 'block'])
ALERT_MSG = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',
                            color='white')
FEEDBACK_O = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
phase = visual.TextStim(win = WIN, text='Practice block.\nPress the "Space" key to continue.', pos=(0, 6), height=0.8)
instr = visual.TextStim(win = WIN,text='Remmber position and color,\nif color belong same frame, press "Left",otherwise color belong diifent frame, press"Right".\n Press "space" to continue.', pos=(0, 4), height=0.8)
practice = visual.TextStim(win = WIN,text='This is the practice block.\n''Make judgment if color appear belong same frame.Press "Left",/n color appears in different frame, please press "Right".''Now press the "Space" key to start practice block.', pos=(0, -2), height=0.8)
COLORS = (0, 230, 115),(255, 128, 0),(128, 0, 128),(0, 100, 0),(139, 69, 19) ,(255, 182, 193),(222, 184, 135),(255, 140, 0),(0, 102, 102),(107, 142, 35),(0, 128, 128)
FIX = visual.TextStim(win = WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}

class Block():
    def __init__(self,block, index):
        self.block = block
        self.index = index
class Group(Block):
    def __init__(self,block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz):
        super(Group,self).__init__(self,block,index)
        self.sz = sz
        self.positions = positions
        self.color = color
        self.ups = ups
        self.downs = downs
        self.col_a = col_a
        self.col_b = col_b
        self.col_new = col_new

class Response(Group):
    def __init__(self, category, display_color, probetype,CSI,seq,ans,RT,FEEDBACK,block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz):
        super(Response,self).__init__(block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz)
        self.probetype = probetype
        self.CSI = CSI
        self.seq = seq
        self.category = category
        self.ans = ans
        self.RT = RT
        self.FEEDBACK = FEEDBACK
        self.display_color = display_color
    def drawLearningCues(self):  # make frame need seperately $ Lin: Failed to comprehence.
        if self.seq == 0:
            diam = []
            for j in range(len(self.downs)):
                dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
                diam.append(dim)
            for idx, dim in enumerate(diam):
                dim.setPos(self.downs[idx])
                diam.draw()
            circle = []
            for j in range(len(self.ups)):
                cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
                circle.append(cir)
            for idx, cir in enumerate(circle):
                cir.setPos(self.ups[idx])
                circle.draw()
        else:
            diam = []
            for j in range(len(self.ups)):
                dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
                diam.append(dim)
            for idx, dim in enumerate(diam):
                dim.setPos(self.ups[idx])
                diam.draw()
            circle = []
            for j in range(len(self.downs)):
                cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
                circle.append(cir)
            for idx, cir in enumerate(circle):
                cir.setPos(self.downs[idx])
                circle.draw()
    def drawLearningColors(self):
        squares = []
        for i in range(len(self.positions)):
            squ = visual.Rect(WIN, size=[100, 100], lineColor=None,fillColorSpace='rgb255')
            squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(self.color[idx],'rgb255')
            squ.setPos(self.positions[idx])
            squ.draw()
    def drawProbe(self):
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(self.display_color,'rgb255')
        squ.setPos([0,0])
        squ.draw()
        WIN.flip()
        t1 = core.getTime()
        self.ans = event.waitKeys(keyList=['left', 'right'])
        t2 = core.getTime()
        self.RT =  t2 - t1
        return self.ans, self.RT
    def save_resp(self, ans, RT, cue, display_color, seq, FEEDBACK, sz):
        dataFile = open("%s.csv"%(expInfo['ID']+'_'+expInfo['age']+'_'+expInfo['block']), 'a')
        self.ans = str(ans)
        self.sz = str(sz)
        self.cue = str(cue)
        self.FEEDBACK = str(FEEDBACK)
        self.RT = str(RT)
        self.display_color = str(display_color)
        dataFile.write(ans + ','+ sz +',' + FEEDBACK +','+ seq +','+ RT +',' +display_color +'\n')
def TestingCues(CSI,seq):
    if seq == 0:
        cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
        cir.setPos([0,0])
        cir.draw()
    elif seq == 1:
        dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
        dim.setPos([0,0])
        dim.draw()
    WIN.flip()
    core.wait(CSI)
def get_ans(probetype,ans):
    if probetype == 0 and ans == ['left']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif probetype == 1 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif probetype == 2 and ans == ['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif probetype == 0 and ans == ['right']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif probetype == 1 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif probetype == 2 and ans == ['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif ans == ['left','right'] and ans == ['right','left']:
        FEEDBACK.append('p')
    return Response.FEEDBACK
def decideSZ():
#    for i in range(4):
    sz = sample([1,2,3,4],4)
    return sz
def decideProbeType():
    for i in range(2):
        probetype = sample([0, 0, 1, 2],1)[0]
    return probetype
def decideCSI():
    for i in range(2):
        CSI = sample([.3,2,5],1)[0]
    return CSI
def decideSeq():
    seq = shuffle(0,1)
    return seq
def decidePos(sz):
    up = (100, 200), (100, -200), (-100, 200), (200, 100)
    ups = sample(up,sz)
    down = (200, -100), (-200, 100), (-200, -100), (-100, -200)
    downs = sample(down,sz)
    positions = list(ups,downs)
    return  positions,ups, downs
def decideColors(sz):
    color = sample(COLORS, sz*2)
    col_a = color[1:sz]
    col_b = color[sz:2*sz]
    col_new = list(set(COLORS)- set(color))
    return  col_a, color, col_b, col_new
def getProbeColor(col_b, col_a, col_new, category, probetype):
    if category == 1:  # diamond circle
        col_positive = col_b
        col_intrusion = col_a
    elif category == 0:  # circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if probetype == 0:
        display_color = col_positive[0]
    elif probetype == 1:
        display_color = col_intrusion[0]
    elif probetype == 2:
        display_color = col_new[0]
    return display_color
def component():
    '''repeat 4 time by random, each component has setsize1-4'''
    Group.sz = decideSZ()
    for i in Group.sz:
        Group.positions, Group.ups, Group.downs = decidePos(i)#i=sz
        Group.color, Group.col_a, Group.col_b, Group.col_new = decideColors(i)
        FIX.draw()
        WIN.flip()
        core.wait(.5)
        Response.LearningColors(Group.color,Group.positions)
        Response.category =randint(0, 1)
        Response.drawLearningCues(Response.category)
        for j in enumerate(sample(CASES, 2)):
            Response.cue = j
            Response.CSI = decideCSI()
            Response.probetype = decideProbeType()
            Response.display_color = getProbeColor(Group.color,Group.col_a, Group.col_b, Group.col_new)
            TestingCues(Response.CSI,Response.seq)
            Response.ans, Response.RT = Response.drawProbe(Response.display_color)
            Response.FEEDBACK = get_ans(Response.ans,Response.probetype)
            Response.save_resp(Response.ans, Response.RT, Response.cue, Response.display_color, Response.FEEDBACK, Group.sz[i])
            Response.FEEDBACK.pop()
def main():
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    rounds = 2
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    for i in range(rounds):#total 48
      for i in range(6):
        component() #24 trials

main()
