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
    def __init__(self, positionz, ups, downs, col_new, color, col_b, col_a, context):
        self.positionz = positionz
        self.ups = ups
        self.downs = downs
        self.col_new = col_new
        self.color = color
        self.col_b = col_b
        self.col_a = col_a
        self.context =context

    def drawContent(self):
        squ_ups = []
        for i in range(len(self.ups)):
            squ = visual.Rect(WIN, size=[100, 100], lineColor=None)  # , fillColorSpace='rgb255')
            squ_ups.append(squ)
        for idx, squ in enumerate(squ_ups):
            squ.setPos(self.ups[idx])
            squ.setFillColor(self.col_a[idx], 'rgb255')
            squ.draw()
        squ_downs = []
        for i in range(len(self.downs)):
            squ = visual.Rect(WIN, size=[100, 100], lineColor=None)  # , fillColorSpace='rgb255')
            squ_downs.append(squ)
        for idx, squ in enumerate(squ_downs):
            squ.setPos(self.downs[idx])
            squ.setFillColor(self.col_b[idx], 'rgb255')
            squ.draw()

    def drawContext(self):
        if self.context == 0: #circle up,diamond down
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
        elif self.context == 1:
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
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext):#,col_positive,col_intrusion):
        super(condition, self).__init__(positionz, ups, downs,
                                        col_new, color, col_b, col_a, context)
        self.conds = conds #condiotn decide CSI and probe type
        self.CSI = CSI
        self.TestingContext = TestingContext
        self.probetype = probetype
    def TestingContext(self):
        if self.TestingContext == 0:
            cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
            cir.setPos([0, 0])
            cir.draw()
        elif self.TestingContext == 1:
            dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
            dim.setPos([0, 0])
            dim.draw()
        WIN.flip()
        core.wait(self.CSI)


class Response(condition):
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext,display_color):
        super(Response, self).__init__(positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext)
        self.display_color = display_color
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

class log(Response):
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext,display_color,ans, FEEDBACK,RT):
        super(log).__init__(positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext,display_color)
        self.ans = ans
        self.FEEDBACK = FEEDBACK
        self.RT = RT
    def logData(self):
        dataFile = open("%s.csv" % (expInfo['ID'] + '_' + expInfo['age'] + '_' + expInfo['block']), 'a')
        sz = len(self.positionz)
        dataFile.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(self.context,sz,self.conds,self.CSI, self.probetype,
                                                                             self.ans, self.FEEDBACK,self.RT,
                                                                             self.positionz, self.ups, self.downs,self.display_color, self.col_new,self.color,
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
def choseProbetype():
    probetype = sample([0,0,1,2],1)[0]
    return probetype
def choseCSI(conds):
    if conds % 3 == 0:
        CSI = .3
    elif conds % 3 == 2:
        CSI = 2
    else:
        CSI = 5
    return CSI

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
def defineColor(TestingContext,context,col_a,col_b ,col_positive = None,col_intrusion =None):
    if TestingContext == 0 and context == 0:  # asking circle
        #            PosDiam = 1  # fill col_b
        colDiam = col_b
        #            PosCir = 0  # fill col_a
        colCir = col_a
        col_positive = colCir
        col_intrusion = colDiam
    elif TestingContext == 1 and context == 1:  # asking diamond
        #            PosDiam = 1  # fill col_b
        colDiam = col_a
        #            PosCir = 0  # fill col_a
        colCir = col_b
        col_positive = colDiam
        col_intrusion = colCir
    elif TestingContext == 0 and context == 1:  # asking circle
        #            PosDiam = 1  # fill col_b
        colDiam = col_a
        #            PosCir = 0  # fill col_a
        colCir = col_b
        col_positive = colCir
        col_intrusion = colDiam
    elif TestingContext == 1 and context == 0:  # asking diamond
        #            PosDiam = 1  # fill col_b
        colDiam = col_b
        #            PosCir = 0  # fill col_a
        colCir = col_a
        col_positive = colDiam
        col_intrusion = colCir
    return col_intrusion, col_positive
def getProbeColor(col_new,probetype,col_intrusion, col_positive,display_color = None):
    if probetype == 0:  # positive probe
        display_color = col_positive
    elif probetype == 1:
        display_color = col_intrusion
    elif probetype == 2:
        display_color = col_new
    return display_color
def decideTestingContext():
    TestingContext = randint(0,1)
    if TestingContext ==0:
        TestingContext2 =1
    else:
        TestingContext2 =0
    return  TestingContext,TestingContext2
def Task(elem,conds):
    TestingContext, TestingContext2 = decideTestingContext()
    for i in [TestingContext,TestingContext2]:
        probetype = choseProbetype()
        CSI = choseCSI(conds)
        col_positive, col_intrusion = defineColor(i, elem.context, elem.col_a, elem.col_b)
        display_color = getProbeColor(elem.col_new,probetype,col_intrusion, col_positive)
        print  type(display_color)
        conditions = condition(elem.positionz, elem.ups, elem.downs, elem.col_new, elem.color, elem.col_a,
        elem.col_b, elem.context,conds, CSI, probetype, i)
        cs = conditions
        res = Response(cs.positionz,cs.ups,
                       cs.downs,cs.col_new, cs.color, cs.col_a, cs.col_b,
                       cs.context,cs.conds,cs.CSI, cs.probetype,
                       cs.TestingContext,display_color)
        res.TestingContext()
        ans, RT= res.ProbeContent()
        WIN.flip()
        FEEDBACK = getAns(res.probetype,ans)
        WIN.flip()
        core.wait(.5)

        print  'Acur = {}, Ans= {}, RT={}, probetype = {},CSI = {},' \
               ' conds={},order={},display_color={},{} = color'\
            .format(FEEDBACK,
                    res.ans,res.RT,res.probetype,res.CSI,res.conds,
                    res.context,res.display_color,res.color)
        log.logData()
        FEEDBACK.pop()

def fourtrials():
    conditions = choseCondition()
    print  conditions
    for conds in conditions:
        FIX = visual.TextStim(win=WIN, pos=(0, 0), height=80, text='+', color='white')
        FIX.draw()
        WIN.flip()
        core.wait(.8)
        sz = decideSZ(conds)
        context =randint(0,1)
        pos = decidePos(sz)
        cols = decideColor(sz)
        elem = Element(pos[0], pos[1], pos[2], cols[0], cols[1], cols[2], cols[3], context)
        elem.drawContent()
        elem.drawContext()
        WIN.flip()
        core.wait(5)
        Task(elem,conds)
    print  'finish 48 trials'
fourtrials()
def for48():
#    ALERT_MSG.draw()
#    WIN.flip()
#    event.waitKeys(keyList=['space'])
    for i in range(4):
        fourtrials()
#for48()
# for i in range(10):
#     for48()
#0	4	38	0.3	2	['right']	[1]	2.837929353	[(-100	 200)	 (100	 200)	 (200	 -100)	 (-200	 -100)]	[(-100	 200)	 (100	 200)]	[(200	 -100)	 (-200	 -100)]	(255	255	 0)	[(255	255	 0)	 (222	184	 135)	 (0	0	 255)	 (255	0	 0)	 (0	100	 0)	 (0	128	 128)	 (255	182	 193)]	[(0	0	 128)	 (139	69	 19)	 (255	0	 255)	 (128	0	 128)]	[(0	0	 128)	 (139	69	 19)]	[(255	0	 255)	 (128	0	 128)]
#self.order,sz,self.conds,self.CSI, self.probetype,self.ans, self.FEEDBACK,self.RT,self.positionz, self.ups, self.downs,self.display_color, self.col_new, self.color,self.col_a, self.col_b)+
# order = 1
# sz =
