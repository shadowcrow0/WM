from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
from itertools import chain
FEEDBACK = []
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': [1,2,3,4,5,6,'p']}
gui.DlgFromDict(dictionary=expInfo, title='VWM Task-2b', order=['ID', 'age','gender','block'])
COLORS =[(255, 0, 255),(139, 69, 19),(255, 140, 0),(0, 0, 128),(0,100,0.),
          (222, 184, 135),(0, 0, 255),(0, 255, 0),(128, 0, 128),
          (107, 142, 35),(255,0,0)]
WIN = visual.Window((1024, 768), monitor='testMonitor',color="grey", units="pix", fullscr=True)
FEEDBACK_O = visual.TextStim(win = WIN, pos=(0, 4), height=60, text='CORRECT!', color='white')
FEEDBACK_X = visual.TextStim(win = WIN, pos=(0, 4), height=60, text='INCORRECT!', color='white')
FIX = visual.TextStim(win = WIN, text='+', height=120, color='white', pos=(0, 0))
ALERT_MSG = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and word, \nPress "Space" to start.',
                            color='white')
BLOCK_MSG = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='Finish 40 trials, take a rest, if you are ready, \nPress "Space" to start.',
                            color='white')
phase = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='If you are ready, Press "Space" to start.',
                            color='white')
END = visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='End of experiment, Press "Space" to end.',
                            color='white')
PRACTICE= visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='**Practice**\nRemember color and word, \nIf you are ready, Press "Space" to start.',
                            color='white')
REMAIN= visual.TextStim(win = WIN, pos=(0, 4), height=40,
                            text='Last 80trials remains\nIf you are ready, Press "Space" to continue.',
                            color='white')

class Element(object): #initailize the color and position we need in the experiment trials
    def __init__(self, positionz, ups, downs, col_new, color, col_b, col_a, context):
        self.positionz = positionz
        self.ups = ups
        self.downs = downs
        self.col_new = col_new #eliminate color already have been selected
        self.color = color
        self.col_b = col_b
        self.col_a = col_a
        self.context =context

    def drawContent(self):
        squ_ups = []
        for i in range(len(self.ups)): #draw separately by position in the screen
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

    def drawContext(self): #draw the context for later selecting
        # positions of context are determined by random
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
    def TestingContexts(self):
        if self.TestingContext == 0:
            cir =visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
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
        squ = visual.Rect(WIN, size=[100, 100], lineColor=None, fillColorSpace ='rgb255')
        squ.setFillColor(self.display_color)
        squ.setPos([0, 0])
        squ.draw()
        WIN.flip()
        t1 = core.getTime()
        self.ans = event.waitKeys(keyList=['left', 'right'])
        t2 = core.getTime()
        self.RT = t2 - t1
        return self.ans, self.RT

class Log(Response):
    def __init__(self,positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext,display_color,ans, FEEDBACK,RT):
        super(Log,self).__init__(positionz, ups, downs, col_new, color, col_a, col_b,context,
                 conds,CSI, probetype,TestingContext,display_color)
        self.ans = ans
        self.FEEDBACK = FEEDBACK
        self.RT = RT
    def logData(self): #save data
        dataFile = open("{}_{}_{}_{}_2b.csv".format(expInfo['block'],expInfo['ID'] , expInfo['age'] , expInfo['gender']), 'a')
        sz = len(self.positionz)
        dataFile.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(expInfo['block'],self.context,sz,self.conds,self.CSI, self.probetype,
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
    a = [(255, 0, 255),(139, 69, 19),(255, 140, 0),(0, 0, 128),(0,100,0.),
          (222, 184, 135)]
    b = [(0, 0, 255),(0, 255, 0),(128, 0, 128),(107, 142, 35),(255,0,0)]
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
    conditions = sample(range(1,41),40)
    return  conditions
def choseProbetypeold():
    probetype = sample([0,0,1,2],1)[0]
    return probetype
def choseprobetype(conds):
    probetype =sample([0,0,1,2],1)[0]
    return probetype

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
    elem.drawContent() #draw color square
    elem.drawContext() #draw shape of frame
    WIN.flip()
    core.wait(5)
def getAns(probetype,ans): #get answer
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
    elif ans ==  ['left', 'right'] or ans == ['right', 'left']:
        FEEDBACK.append('p')
    return FEEDBACK
def checkOrder(context,TestingContext,col_a,col_b): #define color intrusion and color positive
    col_intrusion = None
    col_positive = None
    if context ==0  and TestingContext ==0:
        col_positive = col_a
        col_intrusion = col_b
    elif context ==1 and TestingContext ==0:
        col_positive = col_b
        col_intrusion = col_a
    elif context ==1 and TestingContext ==1:
        col_positive = col_a
        col_intrusion = col_b
    elif context ==0 and TestingContext ==1:
        col_positive = col_b
        col_intrusion = col_a
    col_intrusion = sample(col_intrusion,1)[0]
    col_positive = sample(col_positive,1)[0]
    return col_positive,col_intrusion
def getProbeColor(context,col_a,col_b , TestingContext ,col_new,probetype):

    if probetype == 0:  # positive probe
        #print 'probetype is positive'
        selected_colors =checkOrder(context,TestingContext,col_a,col_b)
        display = selected_colors[0]
    elif probetype == 1:
        #print 'probetype is intrusion'
        selected_colors = checkOrder(context,TestingContext,col_a,col_b)
        display = selected_colors[1]
    elif probetype == 2:
       #print 'probetype is new'
        display = sample(col_new,1)[0]
    display_color  = display
    return  display_color
def decideTestingContext():
    TestingContext = randint(0,1) #random decide shape of frame in 1st probe
    if TestingContext ==0:
        TestingContext2 =1 #decide 2nd probe
    else:
        TestingContext2 =0
    return  TestingContext,TestingContext2
def probe(elem,conds,CSI):
    TestingContext, TestingContext2 = decideTestingContext()
    for i in [TestingContext,TestingContext2]: #run pair recognition
        probetype = choseprobetype(conds)
        conditions = condition(elem.positionz, elem.ups, elem.downs, elem.col_new, elem.color, elem.col_a,
        elem.col_b, elem.context,conds, CSI, probetype, i)
        cs = conditions #make instance for condition class
        display_color = getProbeColor(cs.context,cs.col_a,cs.col_b , i ,cs.col_new,cs.probetype)
        #chose color is going to present in the probe by probetype and color
        res = Response(cs.positionz,cs.ups,
                       cs.downs,cs.col_new, cs.color, cs.col_a, cs.col_b,
                       cs.context,cs.conds,cs.CSI, cs.probetype,
                       cs.TestingContext,display_color)
        res.TestingContexts()
        ans, RT= res.ProbeContent()
        WIN.flip()
        FEEDBACK = getAns(res.probetype,ans)
        WIN.flip()
        logs = Log(res.positionz, res.ups, res.downs, res.col_new, res.color, res.col_a, res.col_b,res.context,
         res.conds,res.CSI, res.probetype,res.TestingContext,res.display_color,ans, FEEDBACK,RT)
        Log.logData(logs)
        core.wait(.3)
        print  'Acur = {}, Ans= {}, RT={}, probetype = {},CSI = {},' \
               ' display_color={},order={},conds={},{} = color' \
            .format(FEEDBACK,
                    res.ans, res.RT, res.probetype, res.CSI, res.display_color, res.conds,
                    res.context, res.display_color, res.color)
        FEEDBACK.pop()



def balance():
    ''' inti
       if condition =1 run CSI = (.3,2,5)
       if condition =2 run CSI = (2,5,.3)
          condition =3 run CSI = (5,.3,2)
          condition =4 run CSI = (.3,5,2)
          condition =5 run CSI = (2,.3,5)
          condition =6 run CSI = (5,2,.3)
          conditions =p run practice
    each block contains 80 trials, #run 40 trials seperately'''
    def practice(CSI):
        PRACTICE.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        conditions = range(1,9)
        for conds in conditions:
            FIX = visual.TextStim(win=WIN, pos=(0, 0), height=80, text='+', color='white')
            FIX.draw()
            WIN.flip()
            core.wait(.8)
            sz = decideSZ(conds)
            context = randint(0, 1)
            pos = decidePos(sz)
            cols = decideColor(sz)
            elem = Element(pos[0], pos[1], pos[2], cols[0], cols[1], cols[2], cols[3], context)
            studyingList(elem)
            probe(elem,conds,CSI)

    def block(CSI):
        def trials40(CSI):
            conditions = choseCondition()
            for conds in conditions:
                FIX = visual.TextStim(win=WIN, pos=(0, 0), height=80, text='+', color='white')
                FIX.draw()
                WIN.flip()
                core.wait(.8)
                sz = decideSZ(conds)
                context = randint(0, 1)  # decide location of shape of frame
                pos = decidePos(sz)
                cols = decideColor(sz)
                elem = Element(pos[0], pos[1], pos[2], cols[0], cols[1], cols[2], cols[3], context)
                # make instance for element class
                studyingList(elem)
                probe(elem, conds, CSI)
            print  'finish 40 trials'

        trials40(CSI)
        BLOCK_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        phase.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        trials40(CSI)
        phase.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
    if expInfo['block'] ==1:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.3)
        block(2)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(5)
    elif expInfo['block'] ==2:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(2)
        block(5)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.3)
    elif expInfo['block'] ==3:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(5)
        block(.3)
        REMAIN.draw()
        event.waitKeys(keyList=['space'])
        WIN.flip()
        block(2)
    elif expInfo['block'] ==4:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.3)
        block(5)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(2)

    elif expInfo['block'] ==5:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(2)
        block(.3)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(5)
    elif expInfo['block'] ==6:
        practice(2)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(5)
        block(2)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.3)
    elif expInfo['block'] =='p':
        practice(.3)
        ALERT_MSG.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.5)
        block(.2)
        REMAIN.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
        block(.3)
balance()
