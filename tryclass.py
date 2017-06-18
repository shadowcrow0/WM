from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
from itertools import chain
FEEDBACK = []
CASES = [0,1]
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
COLORS = ["#ffb6c1", "#deb887", "#ff8000", "#800080", "#00e673", "#008080", "#ff8c00", "#006666","#006400","#6B8E23","#8b4513"]
FIX = visual.TextStim(win = WIN, text='+', height=120, color='white', pos=(0, 0))
expInfo = {'ID': '', 'age': '', 'gender': ['Male', 'Female'], 'block': ''}

class Block():
    def __init__(self, szs, block, index):
        self.block = block
        self.szs = szs
        self.index = index
        self.setszs()
    def setszs(self):
        szs = sample([1, 2, 3, 4], 4)
        return  szs

class Group(Block):
    def __init__(self,block, index,col_new,col_b ,col_a, downs, ups, color , pos, sz):
        super(Group,self).__init__(self,block,index)
        self.sz = sz
        self.pos = pos
        self.color = color
        self.ups = ups
        self.downs = downs
        self.col_a = col_a
        self.col_b = col_b
        self.col_new = col_new
        self.decidePos(sz)
        self.decideColor(sz)
    def decidePos(self,sz):
        up = [(100, 200), (100, -200), (-100, 200), (200, 100)]
        self.ups = sample(up,sz)
        down = [(200, -100), (-200, 100), (-200, -100), (-100, -200)]
        self.downs = sample(down, sz)
        self.position = list(chain.from_iterable([self.ups, self.downs]))
    def decideColor(self,sz):
        a = ["#ffb6c1", "#deb887", "#ff8000", "#800080", "#00e673"]
        b = ["#008080", "#ff8c00", "#006666", "#006400", "#6B8E23", "#8b4513"]
        h = sample(range(10), 1)[0]
        if h % 2 == 0:
            self.col_a = sample(a, sz)
            self.col_b = sample(b, sz)
            self.color = list(chain.from_iterable([self.col_a, self.col_b]))
            self.col_new = list(set(COLORS)- set(self.color))
        else:
            self.col_b = sample(a, sz)
            self.col_a = sample(b, sz)
            self.color = list(chain.from_iterable([self.col_a, self.col_b]))
            self.col_new = list(set(COLORS)- set(self.color))
        return  self.color, self.col_b, self.col_a, self.col_new

class Response(Group):
    def __init__(self, display_color, probetype,CSI,seq,ans,RT,FEEDBACK,block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz):
        super(Response,self).__init__(block, index,col_new,col_b ,col_a, downs, ups, color, positions, sz)
        self.probetype = probetype
        self.CSI = CSI
        self.seq = seq
        self.ans = ans
        self.RT = RT
        self.FEEDBACK = FEEDBACK
        self.display_color = display_color
        self.decideSeq()
        self.choseCondition()
        self.getProbeColor()
    def decideSeq(self):
        self.seq = randint(0, 1)
        return self.seq
    def choseCondition(self):
        condition = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.conds = sample(condition, 1)
        for self.conds in condition:
            if self.conds % 2 != 0:
                self.probetype = 0
            elif self.conds % 4 == 0:
                self.probetype = 2
            else:
                self.probetype = 1
            if self.conds % 3 == 0:
                self.CSI = int(.3)
            elif self.conds % 3 == 2:
                self.CSI = int(2)
            else:
                self.CSI = int(5)
            return self.CSI, self.probetype
    def getProbeColor(self):
        if self.seq == 1:  # diamond circle
            col_positive = self.col_b
            col_intrusion = self.col_a
        elif self.seq == 0:  # circlediamond
            col_positive = self.col_a
            col_intrusion = self.col_b
        if self.probetype == 0:
            self.display_color = col_positive[0]
        elif self.probetype == 1:
            self.display_color = col_intrusion[0]
        elif self.probetype == 2:
            self.display_color = self.col_new[0]
        return self.display_color
    def drawProbe(self):
        self.display_color = self.getProbeColor()
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(self.display_color)#,'rgb255')
        squ.setPos([0,0])
        squ.draw()
        WIN.flip()
        t1 = core.getTime()
        self.ans = event.waitKeys(keyList=['left', 'right'])
        t2 = core.getTime()
        self.RT =  t2 - t1
        return self.ans, self.RT
    def save_resp(self, ans, RT, display_color, seq, FEEDBACK, color, pos, sz):
        dataFile = open("%s.csv"%(expInfo['ID']+'_'+expInfo['age']+'_'+expInfo['block']), 'a')
        self.ans = str(ans)
        self.sz = str(sz)
        self.seq = str(seq)
        self.FEEDBACK = str(FEEDBACK)
        self.RT = str(RT)
        self.display_color = str(display_color)
        self.color = str(color)
        self.pos = str(pos)
        dataFile.write(ans + ','+ sz +',' + FEEDBACK +','+ seq +','+ RT +',' +display_color +','+color+','+pos+'\n')

    def drawLearningCues(self):  # make frame need seperately $ Lin: Failed to comprehence.
        def drawDiamond(self):
            diam = []
            for j in range(len(self.positions)):
                dim = visual.Rect(WIN, size=(170, 170), ori=45, lineWidth=3)
                diam.append(dim)
            for idx, dim in enumerate(diam):
                dim.setPos(self.positions[idx])
                dim.draw()

        def drawCircle(self):
            circle = []
            for j in range(len(self.positions)):
                cir = visual.Circle(WIN, radius=50, edges=40, lineWidth=3)
                circle.append(cir)
            for idx, cir in enumerate(circle):
                cir.setPos(self.positions[idx])
                cir.draw()
        if self.seq == 0:
            drawCircle(self.ups)
            drawDiamond(self.downs)
        elif self.seq == 1:
            drawDiamond(self.ups)
            drawCircle(self.downs)
    def drawLearningColors(self):
        squares = []
        for j in range(len(self.color)):
            squ =visual.Rect(WIN, size=[100, 100], lineColor=None,fillColorSpace='rgb255')
            squares.append(squ)
        for idx, squ in enumerate(squares):
            squ.setFillColor(self.color[idx],'rgb255')
            squ.setPos(self.positions[idx])
            squ.draw()
    def drawTestingCues(self):
        self.CSI = self.choseCondition()
        if self.seq == 0:
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos([0,0])
            cir.draw()
        elif self.seq == 1:
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos([0,0])
            dim.draw()
        WIN.flip()
        core.wait(self.CSI)
    def get_ans(self):
        if self.probetype == 0 and self.ans == ['left']:
            FEEDBACK_O.draw()
            self.FEEDBACK.append(1)
        elif self.probetype == 1 and self.ans == ['right']:
            FEEDBACK_O.draw()
            self.FEEDBACK.append(1)
        elif self.probetype == 2 and self.ans == ['right']:
            FEEDBACK_O.draw()
            self.FEEDBACK.append(1)
        elif self.probetype == 0 and self.ans == ['right']:
            FEEDBACK_X.draw()
            self.FEEDBACK.append(0)
        elif self.probetype == 1 and self.ans == ['left']:
            FEEDBACK_X.draw()
            self.FEEDBACK.append(0)
        elif self.probetype == 2 and self.ans == ['left']:
            FEEDBACK_X.draw()
            self.FEEDBACK.append(0)
        elif self.ans == ['left','right'] and self.ans == ['right','left']:
            self.FEEDBACK.append('p')
        return self.FEEDBACK


def drawStimulus(seq,downs, ups, pos,color):
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    Response.drawLearningColors(pos,color)
    Response.drawLearningCues(seq,downs, ups)
    WIN.flip()
    core.wait(5)
def recognitionPhase(CSI,seq, ans, display_color,probetype, col_a,col_b,col_new,RT,FEEDBACK, color, pos, sz):
    Response.drawTestingCues(CSI,seq)
    ans,rt = Response.drawProbe(display_color)
    FEEDBACK = Response.get_ans(ans, probetype)
    Response.save_resp(ans, RT, display_color, seq, FEEDBACK, color, pos, sz)
    FEEDBACK.pop()
    WIN.flip()
    core.wait(.8)


def component():
    '''repeat 4 time by random, each component has setsize1-4'''
    szs = sample([1,2,3,4],4)
    for sz in  szs :
        drawStimulus(Response.seq,Response.downs, Response.ups, Response.color)
        for j in enumerate(sample(CASES, 2)):
            Response.cue = j
            recognitionPhase(Response.CSI, Response.seq, Response.ans, Response.display_color, Response.probetype, Response.col_a, Response.col_b, Response.col_new, Response.RT, Response.FEEDBACK, Response.color, Response.pos,
                             Response.sz)
def trials48():
    #    ALERT_MSG.draw()
    #    WIN.flip()
    #    event.waitKeys(keyList=['space'])
    rounds = 2
    #    instr.draw()
    #    WIN.flip()
    #    event.waitKeys(keyList=['space'])
    for i in range(rounds):#total 48
        for i in range(6):
            component() #24 trials
trials48()
