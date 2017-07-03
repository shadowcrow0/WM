from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
from itertools import chain
FEEDBACK = []
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}
gui.DlgFromDict(dictionary=expInfo, title='VWM Task-2', order=['ID', 'age','block'])
COLORS = [(0, 128, 128),(139, 69, 19),(255, 255, 0),(255, 0, 0),(0, 0, 128),(255, 182, 193),(222, 184, 135),(0, 0, 255),(255, 0, 255),(128, 0, 128),(0, 100, 0)]
WIN = visual.Window((1024, 768), monitor='testMonitor',color="grey", units="pix", fullscr=False)
FEEDBACK_O = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(win = WIN, pos=(0, 4), height=30, text='INCORRECT!', color='white')
phase = visual.TextStim(win = WIN, text='Practice block.\nPress the "Space" key to continue.', pos=(0, 6), height=0.8)
instr = visual.TextStim(win = WIN,text='Remember position and color,\nif color belong same frame, press "Left",otherwise color belong diifent frame, press"Right".\n Press "space" to continue.', pos=(0, 4), height=0.8)
practice = visual.TextStim(win = WIN,text='This is the practice block.\n''Make judgment if color appear belong same frame.Press "Left",/n color appears in different frame, please press "Right".''Now press the "Space" key to start practice block.', pos=(0, -2), height=0.8)
FIX = visual.TextStim(win = WIN, text='+', height=120, color='white', pos=(0, 0))
ALERT_MSG = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',
                            color='white')
class Element(object):
    def __init__(self, positionz, ups, downs, col_new, color, col_b, col_a, order):
        self.positionz = positionz
        self.ups = ups
        self.downs = downs
        self.col_new = col_new
        self.color = color
        self.col_b = col_b
        self.col_a = col_a
        self.order =order
    def drawContent(self):
        squares = []
        for i in range(len(self.positionz)):
            squ = visual.Rect(WIN, size=[100, 100], lineColor=None)  # , fillColorSpace='rgb255')
            squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setPos(self.positionz[idx])
            squ.setFillColor(self.color[idx], 'rgb255')
            squ.draw()

    def drawContext(self):
        if self.order == 0:
            circle = []
            for j in range(len(self.ups)):
                cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
                circle.append(cir)
            for idx, cir in enumerate(circle):
                cir.setPos(self.ups[idx])
                cir.draw()
            diam = []
            for j in range(len(self.downs)):
                dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
                diam.append(dim)
            for idx, dim in enumerate(diam):
                dim.setPos(self.downs[idx])
                dim.draw()
        elif self.order == 1:
            diam = []
            for j in range(len(self.ups)):
                dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
                diam.append(dim)
            for idx, dim in enumerate(diam):
                dim.setPos(self.ups[idx])
                dim.draw()
            circle = []
            for j in range(len(self.downs)):
                cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
                circle.append(cir)
            for idx, cir in enumerate(circle):
                cir.setPos(self.downs[idx])
                cir.draw()

class condition(Element):
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,order,
                 conds,CSI, probetype,display_color):
        super(condition, self).__init__(positionz, ups, downs,
                                        col_new, color, col_b, col_a, order)
        self.conds = conds #condiotn decide CSI and probe type
        self.CSI = CSI
        self.probetype = probetype
        self.display_color = display_color

    def TestingContext(self):
        if self.order == 0:
            cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
            cir.setPos([0, 0])
            cir.draw()
        elif self.order == 1:
            dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
            dim.setPos([0, 0])
            dim.draw()
        WIN.flip()
        core.wait(self.CSI)

    def ProbeContent(self):
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None)
        squ.setFillColor(self.display_color  ,'rgb255')
        squ.setPos([0, 0])
        squ.draw()
        WIN.flip()
        t1 = core.getTime()
        self.ans = event.waitKeys(keyList=['left', 'right'])
        t2 = core.getTime()
        self.RT = t2 - t1
        return self.ans, self.RT

class Response(condition):
    def __init__(self,positionz, ups, downs, col_new, color,
                 col_a, col_b,order,
                 conds,CSI, probetype,display_color,ans, FEEDBACK,RT):
        super(Response, self).__init__(positionz, ups, downs,
                                       col_new, color, col_a, col_b,order,
                                       conds,CSI, probetype,display_color)
        self.ans = ans
        self. FEEDBACK = FEEDBACK
        self.RT = RT

    def logData(self):
        dataFile = open("%s.csv" % (expInfo['ID'] + '_' + expInfo['age'] + '_' + expInfo['block']), 'a')
        sz = len(self.positionz)
        dataFile.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(self.order,sz,self.conds,self.CSI, self.probetype,
                                                                             self.display_color,self.ans, self.FEEDBACK,self.RT,
                                                                             self.positionz, self.ups, self.downs, self.col_new, self.color,
                                                                             self.col_a, self.col_b)+'\n')
def decidePos(sz):
    up = [(100, 200), (-200, 100), (-100, 200), (200, 100)]
    ups = sample(up,sz)
    down = [(200, -100), (100, -200), (-200, -100), (-100, -200)]
    downs = sample(down, sz)
    positionz = list(chain.from_iterable([ups, downs]))
    return  positionz,ups, downs
def decideColor(sz):
    a = [(0, 128, 128), (139, 69, 19), (255, 255, 0), (255, 0, 0), (0, 0, 128), (255, 182, 193)]
    b = [(222, 184, 135),(0, 0, 255), (255, 0, 255),(128, 0, 128), (0, 100, 0)]
    h = sample(range(10), 1)[0]
    if h % 2 == 0:
        col_a = sample(a, sz)
        col_b = sample(b, sz)
        colors = list(chain.from_iterable([col_a, col_b]))
        col_new = list(set(COLORS) - set(colors))
    else:
        col_b = sample(a, sz)
        col_a = sample(b, sz)
        colors = list(chain.from_iterable([col_a, col_b]))
        col_new = list(set(COLORS) - set(colors))
    return col_new,colors,col_b,col_a

def choseCondition():
    condition = range(1,49)
    conditions = sample(condition, 48)
    return  conditions
def choseProbetype(conds):
    if conds % 2 != 0:
        probetype = 0
    elif conds % 4 == 0:
        probetype = 2
    else:
        probetype = 1
    return probetype
def choseCSI(conds):
    if conds % 3 == 0:
        CSI = .3
    elif conds % 3 == 2:
        CSI = int(2)
    else:
        CSI = int(5)
    return CSI

def getProbeColor( probetype,cue, col_a, col_b, col_new,col_positive = None,
                   col_intrusion = None,display_color= None):
    if cue == 1:  # diamond circle
        col_positive = col_b
        col_intrusion = col_a
    elif cue == 0:  # circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if probetype == 0:
        display_color = col_positive[0]
    elif probetype == 1:
        display_color = col_intrusion[0]
    elif probetype == 2:
        display_color = col_new[0]
    return display_color
def decideSZ(conds):
    if conds % 4 ==0:
        sz = 4
    elif conds % 4 ==1:
        sz = 1
    elif conds % 4 ==2:
        sz = 2
    else:
        sz =3
    return sz

def decideOrder():
    o= randint(0,1)
    if o ==0:
        o2= 1
    elif o==1:
        o2 = 0
    return o, o2
def studyingList(elem):
    elem.drawContent()
    elem.drawContext()
    WIN.flip()
    core.wait(5)
def getAns(probetype,ans):
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
    elif ans == ['left', 'right'] and ans == ['right', 'left']:
        FEEDBACK.append('p')
    return FEEDBACK

def ProbeStage(elem,o,o2,conds):
    for i in [o,o2]:
        probetype = choseProbetype(conds)
        CSI = choseCSI(conds)
        display_color = getProbeColor(probetype, i, elem.col_a, elem.col_b, elem.col_new)
        conditions = condition(elem.positionz, elem.ups, elem.downs, elem.col_new, elem.color,
                               elem.col_a, elem.col_b, i, conds, CSI, probetype, display_color)
        cs = conditions
        cs.TestingContext()
        ans, RT= cs.ProbeContent()
        WIN.flip()
        FEEDBACK = getAns(cs.probetype,ans)
        WIN.flip()
        core.wait(.8)
        res = Response(cs.positionz,cs.ups,
                       cs.downs,cs.col_new, cs.color, cs.col_a, cs.col_b,
                       cs.order,cs.conds,cs.CSI, cs.probetype,
                       cs.display_color, ans,FEEDBACK,RT)
        print  'Acur = {}, Ans= {}, RT={}, probetype = {},CSI = {},' \
               ' conds={},order={},display_color={},{} = color'\
            .format(res.FEEDBACK,
                    res.ans,res.RT,res.probetype,res.CSI,res.conds,
                    res.order,res.display_color,res.color)
        res.logData()
        FEEDBACK.pop()
def Task(elem,o,o2,conds):
    studyingList(elem)
    ProbeStage(elem,o,o2,conds)
def fourtrials():
    conditions = choseCondition()
    print  conditions
    for conds in conditions:
        FIX = visual.TextStim(win=WIN, pos=(0, 0), height=80, text='+', color='white')
        FIX.draw()
        WIN.flip()
        core.wait(.8)
        sz = decideSZ(conds)
        o, o2 = decideOrder()
        pos = decidePos(sz)
        cols = decideColor(sz)
        elem = Element(pos[0], pos[1], pos[2], cols[0], cols[1], cols[2], cols[3], o)
        Task(elem,o,o2,conds)
    print  'finish 16 trials'

def for48():
    ALERT_MSG.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    for i in range(4):
        fourtrials()
for i in range(10):
    for48()
