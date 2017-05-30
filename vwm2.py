from psychopy import visual, core, event, data, gui
from psychopy.tools.filetools import fromFile, toFile
from itertools import chain
from random import sample
from itertools import product,chain,  islice
import csv
import determine_cue

#INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'block':''}
#gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age','block'])
WIN = visual.Window((1366, 800), color="grey", units="pix",fullscr = False)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(WIN, pos=(0, 4), height=30,text='CORRECT!', color = 'white')
FEEDBACK_X = visual.TextStim(WIN, pos=(0, 4), height=30,text='INCORRECT!', color = 'white')
COLOR = [(0, 230, 115),(255, 128, 0), (128, 0, 128), (0, 100, 0), (139, 69, 19) ,(255, 182, 193), (222, 184, 135), (255, 140, 0), (0, 102, 102), (107, 142, 35) ,(0, 128, 128)]


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
sz = []#setsize, determine how many squares need to present
ProbeType2 = []
CSI2 = []
ProbeType = []
CSI = []
cue = []
thisN = []
thisIndex = []
col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []#down 4 position
cat1 =[]
cat2 = []
FEEDBACK = []
datafile = open("vwm.csv", "rb")
reader = csv.reader(datafile, delimiter=",")
for row in reader:
    sz.append(float(row[0]))
    ProbeType.append(float(row[1]))
    CSI2.append(float(row[2]))
    ProbeType2.append(float(row[3]))
    CSI.append(float(row[4]))
    cue.append(float(row[5]))
    thisIndex.append(int(row[7]))
    cat1.append(row[14])
    cat2.append(row[15])
datafile.close()

datafile = open("a.csv", "rb")
reader = csv.reader(datafile, delimiter=";")
for row in reader:
    col_a.append(row[1])
    color.append(row[0])
    col_b.append(row[2])
    ups.append(row[3])
    pos.append(row[5])
    downs.append(row[4])

##################save file and stimulation
#def save_ans(rt, ans, stoptime, res, category, setsize, FEEDBACK, display_color, col_positive, cols_intrusion, pos_squ, pos_cir, positions,rounds):
#    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']+'_'+INFO['block']), 'a')
#    #dataFile.write('rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK\n')
#    rt = str(rt)
#    ans=str(ans)
#    stoptime=str(stoptime) 
#    res = str(res)
#    category = str(category)
#    setsize = str(setsize)
#    FEEDBACK= str(FEEDBACK)
#    display_color = str(display_color)
#    col_positive = str(col_positive)
#    col_intrusion = str(col_intrusion)
#    pos_squ = str(pos_squ)
#    pos_cir = str(pos_cir)
#    positions = str(positions)
#    rounds = str(rounds)
#    dataFile.write(rt+','+ ans+','+stoptime+','+res+','+ category+','+ setsize+','+ FEEDBACK+','+ display_color+','+col_positive+','+ cols_intrusion +','+ pos_squ+','+ pos_cir+','+ positions +','+ rounds+'\n')
######end of handling data ###########    
################basic component
#determine which position circle and diamond belong, 
#if cue = 0 menas circle up, diamond down
# if cue = 1
#col_a = [(0, 102, 102), (0, 230, 115)]
#color = [(107, 142, 35), (0, 230, 115), (0, 102, 102), (222, 184, 135)]
#col_b = [(0, 102, 102), (222, 184, 135)]
#ups = [(200, 100), (-100, 200)]
#pos = [(200, 100), (-100, 200), (-200, -100), (100, -200)]
#downs = [(-200, -100), (100, -200)]
#COLORS =[(0, 230, 115),(255, 128, 0), (128, 0, 128), (0, 100, 0), (139, 69, 19) ,(255, 182, 193), (222, 184, 135), (255, 140, 0), (0, 102, 102), (107, 142, 35) ,(0, 128, 128)]
#
#sz = 4
#cue = 1
#CSI =.3
#ProbeType =0
#ProbeType2 =2
#CSI2 = 5
#cat1 = 0
#cat2 = 1

def square(color, pos):
    squares = []
    for i in range(len(pos)):
        squ = visual.Rect(WIN, fillColorSpace="rgb255", size=[100, 100],lineColor = None)
        squares.append(squ)
    # 8. draw squares with color.
    for idx, squ in enumerate(squares):
        squ.setFillColor(color[idx])
        squ.setPos(pos[idx])
        squ.draw()


def determine_cue(cat):
    if cat == 0:
        cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
        cir.setPos([0,0])
        cir.draw()
    elif cat == 1:
        dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
        dim.setPos([0,0])
        dim.draw()


def chose_pos(downs,ups,cue):#make frame need seperately
    if cue ==0:
        cir_dim(ups, downs)
    elif cue ==1:
        dim_cir(ups, downs)

def set_cols(COLORS,color,cat1,ProbeType, col_a,col_b):
    color_new = list(chain.from_iterable(set(COLORS) - set(color)))
    cue = cat1
    res = ProbeType
    if cue ==1:#diamond circle
        col_positive= col_b
        col_intrusion = col_a
    elif cue ==0:#circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive[0]
    elif res == 1:
        display_color = col_intrusion[0]
    elif res == 2:
        display_color = col_new[0]
    return display_color
## about cue and position
## if cue = 0 refer ups fill with circle, and downs fill in diamond
## if cue = 1 refer ups -> diamond, downs -> circle
def set_cols2(COLORS,color,cat2,ProbeType2, col_a,col_b):
    color_new = list(chain.from_iterable(set(COLORS) - set(color)))
    cue = cat2 
    res = ProbeType2
    if cue ==1:#diamond circle
        col_positive= col_b
        col_intrusion = col_a
    elif cue ==0:#circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive[0]
    elif res == 1:
        display_color = col_intrusion[0]
    elif res == 2:
        display_color = col_new[0]
    return display_color

def dim(pos1):
    diam = []
    for j in range(len(pos1)):
        dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
        diam.append(dim)
    for idx, dim in enumerate(diam):
        dim.setPos(pos1[idx])
        dim.draw()

def cir(pos2):
    circle = []
    for j in range(len(pos2)):
        cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
        circle.append(cir)
    for idx, cir in enumerate(circle):
        cir.setPos(pos2[idx])
        cir.draw()

def cir_dim(ups, downs):
    dim(pos1 = downs)
    cir(pos2 = ups)

def dim_cir(ups, downs):
    dim(pos1 = ups)
    cir(pos2 = downs)


def cue1(CSI,cat1):
    cat = cat1
    determine_cue(cat)
    WIN.flip()
    core.wait(CSI)

def cue2(CSI2,cat2):
    cat = cat2
    determine_cue(cat)
    WIN.flip()
    core.wait(CSI2)

def probe1(ProbeType,COLORS,color, col_a,col_b, cat1):
    display_color =set_cols(COLORS,color,cat1,ProbeType, col_a,col_b)
    squ = visual.Rect(WIN, size=[100, 100],lineColor =None,pos = [0,0], fillColorSpace="rgb255")
    squ.setFillColor(display_color)
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2-t1)

def probe2(COLORS,color, col_a,col_b,cat2, ProbeType2):
    display_color = set_cols2(COLORS,color,cat2,ProbeType2, col_a,col_b)
    squ = visual.Rect(WIN, size=[100, 100],lineColor =None,pos = [0,0], fillColorSpace="rgb255")
    squ.setFillColor(display_color)
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2-t1)




def get_ans(ans,res):
    if res ==0 and ans == ['left']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==1 and ans ==['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==2 and ans ==['right']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==0 and ans ==['right']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==1 and ans ==['left']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==2 and ans ==['left']:
        FEEDBACK_X.draw() 
        FEEDBACK.append(0)
    elif ans ==['left''right'] and ans == ['right''left']:
        FEEDBACK.append(p)
    return FEEDBACK


#######################################end of component######################





def showInstr():  # show instruction on screen
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    WIN.flip()
#def error():  # (pos-ans). To be noticed, it will return a positive number if the position is at the right side of the answer
#    return myMouse.getPos()[0] - stimList[countTrial]
#
#
def process(downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2,col_a,col_b,pos,cat1,cat2,thisIndex):  # main function reacting to the response of the subject
    square(color, pos)
    chose_pos(downs,ups,cue)
    WIN.flip()
    core.wait(5)
    cue1(CSI,cat1)
    (ans, rt) = probe1(ProbeType, COLORS, color, col_a,col_b, cat1)
    get_ans(ans,res = ProbeType)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    cue2(CSI2,cat2)
    (ans2, rt2, res) = probe2(ProbeType2,COLORS,color, col_a,col_b, cat2)
    get_ans(ans,res = ProbeType2)
    WIN.flip()
    core.wait(.8)
    FEEDBACK.pop()
    print thisIndex
process(downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2,col_a,col_b,pos,cat1,cat2,thisIndex)
def main():
    global sz,downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2,col_a, col_b, pos ,thisIndex
    ## Experiment Section, use experiment variables here
    print(color)
    rounds =80
    for i in range(rounds):
        process(sz = sz[i],ProbeType = ProbeType[i],CSI = CSI[i] ,ProbeType2 = ProbeType2[i], CSI2 = CSI2[i],cue = cue[i],color = color[i],col_a = col_a[i], col_b = col_b[i],pos = pos[i], ups = ups[i],downs = downs[i],thisIndex = thisIndex[i])
main()
## Experiment Section, use experiment variables here
    print("color = {}, col_a = {}, col_b = {}, pos = {}, ups ={}, downs ={}".format(color[i], col_a[i], col_b[i], pos[i], ups[i], downs[i]))
    print("sz = {} , ProbeType = {}, CSI = {}, ProbeType2 ={}, CSI2 ={}, cue = {}, thisIndex={}".format(sz[i],ProbeType[i], CSI[i], ProbeType2[i],CSI2[i],cue[i],thisIndex[i]))

    for i in range(rounds):
    #    print('Trial {}. Click at [{:4f}]. RT : {:3f} sec. '
    #          'Error: {:3f}. Status: {}. Color: {}.'.format(
    #              countTrial+1, myMouse.getPos()[0], myMouse.mouseMoveTime(),
    #              error(), status, arrowAns.fillColor))  # for debug
        square(color, pos)
        chose_pos(downs,ups,cue)
        WIN.flip()
        core.wait(5)
        cue1(CSI,cat1)
        (ans, rt) = probe1(ProbeType, COLORS, color, col_a,col_b, cat1)
        get_ans(ans,res = ProbeType)
        WIN.flip()
        core.wait(.8)
        FEEDBACK.pop()
        cue2(CSI2,cat2)
        (ans2, rt2, res) = probe2(ProbeType2,COLORS,color, col_a,col_b, cat2)
        get_ans(ans,res = ProbeType2)
        WIN.flip()
        core.wait(.8)
        FEEDBACK.pop()
        print thisIndex
        trials.addData('sz', sz[i])  # as countTrial is counting from 0, there should be a "+1"
        trials.addData('ProbeType', thisBlock)
        trials.addData('CSI', myMouse.getPos()[0])
        trials.addData('ProbeType2', stimList[countTrial])
        trials.addData('CSI2', status)  # hit/ miss
        trials.addData('cue', error())  # see the error function above
        trials.addData('rt1', myMouse.mouseMoveTime())
        trials.addData('cat1', arrowAns.fillColor)
        trials.addData('cat2',)
        trials.addData('col_a',)
        trials.addData('col_b',)
        trials.addData('color',)
        trials.addData('pos',)
        trials.addData('ups',)
        trials.addData('downs',)
        trials.addData('rt2',)
        print("color = {}, col_a = {}, col_b = {}, pos = {}, ups ={}, downs ={}".format(color[i], col_a[i], col_b[i], pos[i], ups[i], downs[i]))
        print("sz = {} , ProbeType = {}, CSI = {}, ProbeType2 ={}, CSI2 ={}, cue = {}, thisIndex={}".format(sz[i],ProbeType[i], CSI[i], ProbeType2[i],CSI2[i],cue[i],thisIndex[i]))

        
        
    # show hit/miss and also the correct answer
    #    arrowAns.draw()
    #    myWin.flip()
    #    # wait for 1200ms and erase them all
    #    core.wait(1.2)
    #    myWin.flip()
    #    # reset mouse status
    #    myMouse.mouseMoved(reset=True)
    #
    # prepare the stimuli in those blocks
    #blocks = []
    #for _ in range(blockNum):
    #    blocks.append(list(sti()))
    #
    #while True:  # here goes the experiment
    #    for thisBlock, content in enumerate(blocks):
    #        # show up the screen
    #        phase.draw()
    #        myWin.flip()
    #        if thisBlock == 0:  # practice before first block
    #
    # start practicing
    #            event.waitKeys(keyList=['space'])
    #            showInstr()
    #            thisTraining = 0
    #            while thisTraining < 2:  # two training
    #                practice.draw()
    #                arrowAns.draw()
    #                myWin.flip()
    #                event.waitKeys(keyList=['space'])
    #                # respond correctly (-10 and 10 respectively)
    #                if abs(myMouse.getPos()[0] - [-10, 10][thisTraining]) <= radiusAE:
    #                    arrowAns.pos = [10, arrowAns.pos[1]]
    #                    thisTraining += 1
    #                    practice.setText('Good. Here goes one more try.')
    #                else:  # too far away from answer
    #                    pass
    #            practice.setAutoDraw(False)
    #            arrowAns.setAutoDraw(False)
    #            print('observer_ID: {}'.format(int(expInfo['observer_ID'])))
    #        phase.setText('Test block.\nPress the "Space" key to continue.')
    #        phase.draw()
    #        myWin.flip()
    #        event.waitKeys(keyList=['space'])
    #        showInstr()
    #        # add test stimuli into experiment
    #        stimList = content
    #        trials = data.TrialHandler(  # exclude the last one, for which represents the color only
    #            stimList[:-1], 1, method='sequential',
    #            dataTypes=['seq', 'block', 'pos', 'ans', 'acc', 'err', 'rt', 'col'])
    #        exp.addLoop(trials)
    #        # add transfer stimuli into experiment
    #        sequence = rand.sample(xrange(4), 4)
    #        n = [[[-7.5, stimList[68]], [stimList[67], stimList[68]]],
    #             [[stimList[2], stimList[3]], [stimList[26], stimList[27]]],
    #             [[stimList[8], stimList[9]], [stimList[20], stimList[21]]],
    #             [[stimList[13], stimList[14]], [7.5, stimList[14]]]]
    #        color = ['Green', 'Red', 'Red', 'Green', 'Red', 'Green', 'Green', 'Red'] * 2
    #        direction = ['Up', 'Down', 'Down', 'Up', 'Down', 'Up', 'Up', 'Down',
    #                     'Down', 'Up', 'Up', 'Down', 'Up', 'Down', 'Down', 'Up']
    #        #
    #        tranSeq = [[col[direction[x] == 'Down'] if y % 2 else color[x],
    #                    n[sequence[x % 4]][direction[x] == 'Down'][y],
    #                    direction[x]] for x in range(16) for y in range(2)]
    #        count = range(len(tranSeq)/2)
    #        transfer = [x for x in count for _ in range(predNum + 1)]
    #        prediction = data.TrialHandler(
    #            transfer, 1, method='sequential',
    #            dataTypes=['seq', 'block', 'pos', 'ans', 'direction', 'rt', 'col'])
    #        exp.addLoop(prediction)
    #        # exp start
    #        countTrial = 0
    #        myMouse.mouseMoved(reset=True)
    #        for thisTrial in trials:
    #            event.waitKeys(keyList=['space'])
    #            if abs(error()) <= radiusAE:  # error <= acceptable range
    #                # show "HIT!" on top of the screen
    #                status = 'hit'
    #                hit.draw()
    #                process()
    #            elif abs(error()) > radiusAE:  # error > acceptable range
    #                # show "MISS!" on top of the screen
    #                status = 'miss'
    #                miss.draw()
    #                process()
    #            countTrial += 1
    #            exp.nextEntry()
    #        phase.setText('Transfer block.\nPress the "Space" key to continue.')
    #        phase.draw()
    #        myWin.flip()
    #        event.waitKeys(keyList=['space'])
    #        showInstr()
    #        seq = 0  # the answer order, indicating the next N_th prediction
    #        for target, content in enumerate(tranSeq):
    #            if not target % 2:  # for even in zero-based numbering
    #                tranInstr.draw()
    #                myWin.flip()
    #                event.waitKeys(keyList=['space'])
    #                myMouse.mouseMoved(reset=True)
    #                arrowAns.pos = [content[1], arrowAns.pos[1]]
    #                arrowAns.fillColor = content[0]
    #                arrowAns.draw()
    #                myWin.flip()
    #                core.wait(1.5)
    #                print('Target: {}. seq {}. Color: {}.'.format(
    #                            target/2 + 1, 0, arrowAns.fillColor)) #for debug
    #                prePos = myMouse.getPos()[0]
    #                prediction.addData('seq', -1)
    #                prediction.addData('block', target/2)
    #                prediction.addData('ans', arrowAns.pos[0])
    #                prediction.addData('col', content[0])
    #                prediction.addData('direction', content[2])
    #                exp.nextEntry()
    #            else: 
    #                for seq in range(predNum):
    #                    myMouse.mouseMoved(reset=True)
    #                    if seq == 0:
    #                        arrowAns.pos = [content[1], arrowAns.pos[1]]
    #                    else:
    #                        arrowAns.pos = [prePos, arrowAns.pos[1]]  #! should be modified
    #                    arrowAns.fillColor = content[0]
    #                    arrowAns.draw()
    #                    tranInd.setText('Next {}.'.format(seq + 1))
    #                    tranInd.draw()
    #                    myWin.flip()
    #                    event.waitKeys(keyList=['space'])
    #                    print('Target: {}. seq {}. Click at [{:4f}]. '
    #                           'RT : {:3f} sec. Color: {}.'.format(
    #                                target/2 + 1, seq + 1, myMouse.getPos()[0],
    #                                 myMouse.mouseMoveTime(), arrowAns.fillColor)) #for debug
    #                    prePos = myMouse.getPos()[0]
    #                    prediction.addData('seq', seq)
    #                    prediction.addData('block', target/2)
    #                    prediction.addData('pos', prePos)
    #                    prediction.addData('ans', arrowAns.pos[0])
    #                    prediction.addData('rt', myMouse.mouseMoveTime())
    #                    prediction.addData('col', content[0])
    #                    prediction.addData('direction', content[2])
    #                    myWin.flip()
    #                    core.wait(1)
    #                    exp.nextEntry()
    #        arrowAns.setAutoDraw(False)
    #    numberLine.setAutoDraw(False)
    #    instr.setText('The experiment is finished.\nPlease call the experimenter.')
    #    instr.draw()
    #    print('Participant {} finished the experiment.'.format(int(expInfo['observer_ID'])))
    #    myWin.flip()
    #    event.waitKeys(keyList=['q'])  # press "q" to exit the experiment
    #    # exit the program
    #    myWin.close()
    #    core.quit()
