from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
from itertools import chain
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
COLORS = ["#ffb6c1", "#deb887", "#ff8000", "#800080", "#00e673", "#008080", "#ff8c00", "#006666","#006400","#6B8E23","#8b4513"]
FIX = visual.TextStim(win = WIN, text='+', height=120, color='white', pos=(0, 0))
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
    def __init__(self, display_color, probetype,CSI,seq,ans,RT,FEEDBACK,block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz):
        super(Response,self).__init__(block, index,col_new,col_b ,col_a, downs, ups, color, positions, sz)
        self.probetype = probetype
        self.CSI = CSI
        self.seq = seq
        self.ans = ans
        self.RT = RT
        self.FEEDBACK = FEEDBACK
        self.display_color = display_color
        self.get_ans()
        self.getProbeColor()
        self.drawProbe()
        self.decidePos()
        self.decideColors()
        self.decideSz()
    def decideSz(self):
        self.sz = sample([1,2,3,4],4)
        return self.sz
    def decidePos(self):
        self.sz = self.decideSz()
        for i in self.sz:
            up = (100, 200), (100, -200), (-100, 200), (200, 100)
            self.ups = sample(up,self.sz)
            down = (200, -100), (-200, 100), (-200, -100), (-100, -200)
            self.downs = sample(down,self.sz)
            self.positions = list(chain.from_iterable([self.ups, self.downs]))
        return self.positions, self.ups, self.downs
    def decideColors(self):
        self.sz = self.decideSz()
        for i in self.sz:
            self.color = sample(COLORS, self.sz*2)
            self.col_a = self.color[0:self.sz]
            self.col_b = self.color[self.sz:2*self.sz]
            self.col_new = list(set(COLORS)- set(self.color))
        return  self.col_a, self.color, self.col_b, self.col_new
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
    def decideSeq(self):
        self.seq = sample(CASES, 2)
        return self.seq
    def decideProbeType(self):
        for i in range(2):
            self.probetype = sample([0, 0, 1, 2],1)[0]
        return self.probetype
    def decideCSI(self):
        for i in range(2):
            self.CSI = int(sample([.3,2,5],1)[0])
        return self.CSI
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
        cir.setPos(positions[idx])
        cir.draw()
def drawLearningCues(seq,downs, ups):  # make frame need seperately $ Lin: Failed to comprehence.
    if seq == 0:
        drawCircleCue(ups)
        drawDiamondCue(downs)
    else:
        drawDiamondCue(ups)
        drawCircleCue(downs)
def drawLearningColors(positions,color):
    squares = []
    for j in range(len(color)):
        squ =visual.Rect(WIN, size=[100, 100], lineColor=None,fillColorSpace='rgb255')
        squares.append(squ)
    for idx, squ in enumerate(squares):
        squ.setFillColor(color[idx],'rgb255')
        squ.setPos(positions[idx])
        squ.draw()
def drawTestingCues(CSI,seq):
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
def drawStimulus(seq,downs, ups, positions,color):
    FIX.draw()
    WIN.flip()
    core.wait(.5)
    drawLearningCues(seq,downs, ups)
    drawLearningColors(positions,color)
    WIN.flip()
    core.wait(5)
def recognitionPhase(CSI, seq, display_color,probetype):
    Response.CSI = Response.decideCSI()
    Response.seq = Response.decideSeq()
    Response.probetype = Response.decideProbeType()
    drawTestingCues(Response.CSI,Response.seq)
    Response.display_color = Response.getProbeColor()
    Response.ans, Response.rt = Response.drawProbe(Response.display_color)
    Response.FEEDBACK = Response.get_ans(Response.ans,Response.probetype)
    Response.save_resp(Response)
    FEEDBACK.pop()
    WIN.flip()
    core.wait(.8)
def component(Response):
    '''repeat 4 time by random, each component has setsize1-4'''
    Response.sz = Response.decideSz(Response)
    Response.positions, Response.ups, Response.downs = Response.decidePos()#i=sz
    Response.color, Response.col_a, Response.col_b, Response.col_new = Response.decideColors()
    drawStimulus(Response.seq,Response.downs, Response.ups, Response.positions,Response.color)
    for j in enumerate(Response.seq):
        Response.cue = j
        recognitionPhase(Response.display_color,Response.cue, Response.probetype,Response.CSI)
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
            component(Response) #24 trials
trials48()
