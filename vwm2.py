from itertools import product, chain,  islice
from random import sample, shuffle, randint
from psychopy import core, event, gui, visual, data, info
FEEDBACK = []
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
    def decideSZ(self):
        self.sz = shuffle(range(4))
    def decidePos(self):
        up = (100, 200), (100, -200), (-100, 200), (200, 100)
        self.ups = sample(up,self.sz)
        down = (200, -100), (-200, 100), (-200, -100), (-100, -200)
        self.downs = sample(down,self.sz)
        self.pos = (self.ups,self.downs)
        return  self.pos,self.ups, self.downs
    def decideColors(self):
        self.color = sample(COLORS, self.sz*2)
        self.col_a = self.color[1:self.sz]
        self.col_b = self.color[self.sz:2*self.sz]
        self.col_new = list(set(COLORS)- set(self.color))
class Response(Group):
    def __init__(self, category, display_color, probetype,CSI,seq,ans,RT,Feedback,block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz):
        super(Response,self).__init__(block, index,col_new,col_b ,col_a, downs, ups, color , positions, sz)
        self.probetype = probetype
        self.CSI = CSI
        self.seq = seq
        self.category = category
        self.ans = ans
        self.RT = RT
        self.FEEDBACK = FEEDBACK
        self.display_color = display_color
    def decideProbeType(self):
        for i in range(2):
            self.probetype = sample([0, 0, 1, 2],1)[0]
        return self.probetype
    def decideCSI(self):
        for i in range(2):
            self.CSI = sample([.3,2,5],1)[0]
        return self.CSI
    def decideSeq(self):
        self.seq = shuffle(0,1)
    def drawLearningCues(self):
        if self.category == 0:
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos(self.ups)
            cir.draw()
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos(self.downs)
            dim.draw()
        elif self.category == 1:
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos(self.ups)
            dim.draw()
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos(self.downs)
            cir.draw()
    def LearningSquare(self, color=None):
        if color == None:
            color = self.color
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(color, 'rgb255')
        squ.setPos(self.positions)
        squ.draw()
    def getProbeColor(self):
        if self.category == 1:  # diamond circle
            col_positive = self.col_b
            col_intrusion = self.col_a
        elif self.category == 0:  # circlediamond
            col_positive = self.col_a
            col_intrusion = self.col_b
        if self.probetype == 0:
            self.display_color = col_positive[0]
        elif self.probetype == 1:
            self.display_color = col_intrusion[0]
        elif self.probetype == 2:
            self.display_coloself.col_new[0]
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
    def save_resp(self,ans, RT, seq, display_color, FEEDBACK, probeseq, sz):
        dataFile = open("%s.csv"%(expInfo['ID']+'_'+expInfo['age']+'_'+expInfo['block']), 'a')
        self.ans = str(ans)
        self.sz = str(sz)
        self.seq = str(seq)
        self.FEEDBACK = str(FEEDBACK)
        self.RT = str(RT)
        self.display_color = str(display_color)
        dataFile.write(ans + ','+ sz +',' + FEEDBACK +','+ probeseq +','+ RT +',' +display_color +'\n')

def trial():
    selected_color, col_a, col_b, col_new = Group.decideColors()
    selected_pos, ups, downs = Group.decidePos()
    Probetype = Response.decideProbeType()
    CSI = Response.decideCSI()
    display_color = Response.getProbeColor()
    Probetype2= Response.decideProbeType()
    CSI2 = Response.decideCSI()
