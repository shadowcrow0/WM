from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
from itertools import chain
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}
COLORS = ["#ffb6c1", "#deb887", "#ff8000", "#800080", "#00e673", "#008080", "#ff8c00", "#006666","#006400","#6B8E23","#8b4513"]
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
        self.color = color
        self.col_b = col_b
        self.col_a = col_a
        self.col_new = col_new
        self.positionz = positionz
        self.ups = ups
        self.downs = downs
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
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,conds,CSI, probetype,order):
        super(condition, self).__init__(order,positionz, ups, downs, col_new, color, col_a, col_b)
        self.conds = conds #condiotn decide CSI and probe type
        self.probetype = probetype
        self.CSI = CSI
    def TestingContext(self):
        if self.cue == 0:
            cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
            cir.setPos([0, 0])
            cir.draw()
        elif self.cue == 1:
            dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
            dim.setPos([0, 0])
            dim.draw()
        WIN.flip()
        core.wait(self.CSI)

class Response(condition):
    def __init__(self,ans, FEEDBACK,RT,positions, ups, downs, col_new, color, col_a, col_b,conds,CSI, probetype,display_color, probe_seq):
        super(Response, self).__init__(condition)
        self.ans = ans
        self. FEEDBACK = FEEDBACK
        self.RT = RT
        self.display_color = display_color

    def ProbeContent(self):
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None)
        squ.setFillColor(self.display_color)  # ,'rgb255')
        squ.setPos([0, 0])
        squ.draw()
        WIN.flip()
        t1 = core.getTime()
        self.ans = event.waitKeys(keyList=['left', 'right'])
        t2 = core.getTime()
        self.RT = t2 - t1
        return self.ans, self.RT


def decidePos(sz):
    up = [(100, 200), (-200, 100), (-100, 200), (200, 100)]
    ups = sample(up,sz)
    down = [(200, -100), (100, -200), (-200, -100), (-100, -200)]
    downs = sample(down, sz)
    positionz = list(chain.from_iterable([ups, downs]))
    return  positionz,ups, downs
def decideColor(sz):
    a = ["#ffb6c1", "#deb887", "#ff8000", "#800080", "#00e673"]
    b = ["#008080", "#ff8c00", "#006666", "#006400", "#6B8E23", "#8b4513"]
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
    condition = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    conds = sample(condition, 1)[0]
    return  conds
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

def getProbeColor( probetype,cue, col_a, col_b, col_new,col_positive = None,col_intrusion = None,display_color= None):
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
def get_ans(probetype,ans, FEEDBACK= None):
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

def decideSZ():
    pass
def decideOrder():
    o= [0,1]
    order = sample(o,1)
    order2 = list(set(o) - set(order))
    return order, order2
orders =decideOrder()
sz = 3
pos = decidePos(sz)
cols = decideColor(sz)
elem = Element(pos[0],pos[1],pos[2],cols[0],cols[1],cols[2],cols[3],orders[0])
def studyingList(elem):
    elem.drawContent()
    elem.drawContext()
    WIN.flip()
    core.wait(5)
studyingList(elem)
for i in range(10):
    conds = choseCondition()
    probetype = choseProbetype(conds)
    CSI = choseCSI(conds)
    print CSI, probetype
conditions = condition(elem.positionz,elem.ups,elem.downs,elem.col_a,elem.col_b,elem.color,elem.col_new,conds,probetype, CSI,orders[0])


def getAns(condi, probetype,ans, FEEDBACK= None):
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
def logData():
    pass
def Pairprobes():
    pass
def Task():
    studyingList()
    Pairprobes()
