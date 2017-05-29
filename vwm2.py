from psychopy import visual, core, event, data, gui
from psychopy.tools.filetools import fromFile, toFile
from itertools import chain
from random import sample
from itertools import product,chain
import csv

INFO = { 'ID': '', 'age': '', 'gender': ['Male', 'Female'],'block':''}
gui.DlgFromDict(dictionary=INFO, title='VWM Task', order=['ID', 'age','block'])
WIN = visual.Window((1366, 800), color="grey", units="pix",fullscr = True)
ALERT_MSG = visual.TextStim(WIN, pos=(0, 4), height=40,
                            text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.', color = 'white')
FIX = visual.TextStim(WIN, text='+', height=120, color='white', pos=(0, 0))
FEEDBACK_O = visual.TextStim(WIN, pos=(0, 4), height=30,text='CORRECT!', color = 'white')
FEEDBACK_X = visual.TextStim(WIN, pos=(0, 4), height=30,text='INCORRECT!', color = 'white')
cat = sample([0,1],2)

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
up = []#top 4 positions
pos = []#all position
down = []#down 4 position
datafile = open("vwm.csv", "rb")
reader = csv.reader(datafile, delimiter=",")
for row in reader:
    sz.append(float(row[0]))
    ProbeType.append(float(row[1]))
    CSI2.append(float(row[2]))
    ProbeType.append(float(row[3]))
    CSI.append(float(row[4]))
    cue.append(float(row[5]))
    col_a.append(row[9])
    color.append(float(row[10]))
    col_b.append(row[11])
    ups.append(row[12])
    pos.append(row[13])
    downs.append(row[14])
    thisIndex.append(row[8])
main()
def main():
    ## Experiment Section, use experiment variables here
    for trial in range(len(sz)):
        sz = sz[trial]
        ProbeType = ProbeType[trial]
        CSI = CSI[trial]
        ProbeType2 = ProbeType2[trail]
        CSI2 = CSI2[trial]
        cue = cue[trial]
        color = color[trial]
        col_a = col_a[trial]
        col_b = col_b[trial]
        pos = pos[trial]
        ups = ups[trial]
        downs =downs[trial]
        thisIndex = thisIndex[trial]
        trial(sz,downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2)

## Experiment Section, use experiment variables here
#for trial in range(len(size)):
#    print("size = {}, color = {}".format(size[trial], color[trial]))
    
##################save file and stimulation
def save_ans(rt, ans, stoptime, res, category, setsize, FEEDBACK, display_color, col_positive, cols_intrusion, pos_squ, pos_cir, positions,rounds):
    dataFile = open("%s.csv"%(INFO['ID']+'_'+INFO['age']+'_'+INFO['block']), 'a')
    #dataFile.write('rt, ans, stoptime, res, situation,SET_SIZE, FEEDBACK\n')
    rt = str(rt)
    ans=str(ans)
    stoptime=str(stoptime) 
    res = str(res)
    category = str(category)
    setsize = str(setsize)
    FEEDBACK= str(FEEDBACK)
    display_color = str(display_color)
    col_positive = str(col_positive)
    col_intrusion = str(col_intrusion)
    pos_squ = str(pos_squ)
    pos_cir = str(pos_cir)
    positions = str(positions)
    rounds = str(rounds)
    dataFile.write(rt+','+ ans+','+stoptime+','+res+','+ category+','+ setsize+','+ FEEDBACK+','+ display_color+','+col_positive+','+ cols_intrusion +','+ pos_squ+','+ pos_cir+','+ positions +','+ rounds+'\n')
######end of handling data ###########    
################basic component
#determine which position circle and diamond belong, 
#if cue = 0 menas circle up, diamond down
# if cue = 1
def chose_pos(sz,downs,ups,cue):#make frame need seperately
    circle = []
    diam = []
    if cue ==0:
        for i in range(sz):
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos(ups)
            cir.draw()
            circle.append(cir)
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos(downs)
            dim.draw()
            diam.append(dim)
    elif cue ==1:
        for i in range(sz):
            dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
            dim.setPos(ups)
            dim.draw()
            diam.append(dim)
            cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
            cir.setPos(downs)
            cir.draw()
            circle.append(cir)

def determine_cue(cue):
    if cue == 0:
        cir = visual.Circle(WIN, radius = 50, edges = 40, lineWidth = 3)
        cir.setPos([0,0])
        cir.draw()
    elif cue == 1:
        dim = visual.Rect(WIN, size=(170,170), ori =45, lineWidth =3 )
        dim.setPos([0,0])
        dim.draw()

def square(color,pos):
    squares = []
    for i in range(len(color)):
        squ = visual.Rect(WIN, size=[100, 100],lineColor =None)
        squ.setFillColor(color, 'rgb255')
        squ.setPos(pos)
        squ.draw()
        squares.append(squ)

def probe1():
    res = ProbeType
    set_cols(COLORS,color,cue, col_a,col_b)
    squ = visual.Rect(WIN, size=[100, 100],lineColor =None,pos = [0,0])
    squ.setFillColor(display_color, 'rgb255')
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2-t1.res)

def probe2():
    res = ProbeType2
    set_cols(COLORS,color,cue, col_a,col_b)
    squ = visual.Rect(WIN, size=[100, 100],lineColor =None,pos = [0,0])
    squ.setFillColor(display_color, 'rgb255')
    squ.draw()
    WIN.flip()
    t1 = core.getTime()
    ans = event.waitKeys(keyList=['left', 'right'])
    t2 = core.getTime()
    return (ans, t2-t1,res)



def get_ans(ans,res):
    if res ==0 and ans == ['s']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==1 and ans ==['k']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==2 and ans ==['k']:
        FEEDBACK_O.draw()
        FEEDBACK.append(1)
    elif res ==0 and ans ==['k']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==1 and ans ==['s']:
        FEEDBACK_X.draw()
        FEEDBACK.append(0)
    elif res ==2 and ans ==['s']:
        FEEDBACK_X.draw() 
        FEEDBACK.append(0)
    elif ans ==['s''k'] and ans == ['k''s']:
        FEEDBACK.append(p)
    return FEEDBACK
## about cue and position
## if cue = 0 refer ups fill with circle, and downs fill in diamond
## if cue = 1 refer ups -> diamond, downs -> circle
def set_cols(COLORS,color,cue, col_a,col_b):
    color_new = list(set(COLORS) - set(color))
    if cue ==1:#diamond circle
        col_positive= col_b
        col_intrusion = col_a
    elif cue ==0:#circlediamond
        col_positive = col_a
        col_intrusion = col_b
    if res == 0:
        display_color = col_positive
    elif res == 1:
        display_color = col_intrusion
    elif res == 2:
        display_color = col_new
    return display_color
#######################################end of component######################
def sti(sz,downs, ups, color, cue):  # generate array for later stimuli
    chose_pos(sz,downs,ups,cue)
    square(color,pos)
    WIN.flip()
    core.wait(5)
    
def cue1(CSI):
    cue = cat[0]
    determine_cue(cue)
    WIN.flip()
    core.wait(CSI)

def cue2(CSI2):
    cue = cat[1]
    determine_cue(cue)
    WIN.flip()
    core.wait(CSI2)




def showInstr():  # show instruction on screen
    instr.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    WIN.flip()
#def error():  # (pos-ans). To be noticed, it will return a positive number if the position is at the right side of the answer
#    return myMouse.getPos()[0] - stimList[countTrial]
#
#
def trial(sz,downs, ups, color, cue, CSI, ProbeType, ProbeType2, CSI2):  # main function reacting to the response of the subject
    sti(sz,downs, ups, color, cue)
    cue1(CSI)
    (ans,rt,res) = probe1(res = ProbeType)
    get_ans(ans)
    WIN.flip()
    core.wait(.8)
    cue2(CSI2)
    (ans,rt,res) =probe2(res = ProbeType2)
    get_ans(ans,res)
    WIN.flip()
    core.wait(.8)


#
#    print('Trial {}. Click at [{:4f}]. RT : {:3f} sec. '
#          'Error: {:3f}. Status: {}. Color: {}.'.format(
#              countTrial+1, myMouse.getPos()[0], myMouse.mouseMoveTime(),
#              error(), status, arrowAns.fillColor))  # for debug
#    trials.addData('seq', countTrial+1)  # as countTrial is counting from 0, there should be a "+1"
#    trials.addData('block', thisBlock)
#    trials.addData('pos', myMouse.getPos()[0])
#    trials.addData('ans', stimList[countTrial])
#    trials.addData('acc', status)  # hit/ miss
#    trials.addData('err', error())  # see the error function above
#    trials.addData('rt', myMouse.mouseMoveTime())
#    trials.addData('col', arrowAns.fillColor)
#    # show hit/miss and also the correct answer
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
