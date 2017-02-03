from random import sample
import time
import sys
from psychopy import core, event, gui, visual, data
info = {'cond':['2000ms','1000ms'],'sID':'', 'age':'','gender':['Male','Female'], 'IntruC':['.3','2'],'setsize':['2']}
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title = 'VisualWorkingMemory', 
                          order = ['sID','cond','age'])
if infoDlg.OK == False:
    core.quit()
#####################background######################################
win = visual.Window([800,600],color = "black", units = 'pix')
# 1. define 2 Colors
colors = ['white','#FF0000', '#FFA500']
#1.1 define color appear in response trial
cols = sample(colors[1:],2)
color1s = sample(colors[1:], 2)
# 2. define 2 positions.
pos = [
    [-100,100],
    [100,100]
    ]
pos1s = sample(pos,2)
t = [.3, 2.0]
Ts = sample(t,2)
practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task. \nPress the "Space" key to start.',pos=(0,4),height= 30)
practiceVWM.draw()
win.flip()
event.waitKeys(keyList = 'space')
fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
fix.draw()
win.flip()
core.wait(.5)
t1 = core.getTime()
# 7. draw shape and wait 2000ms
squares = []
for i in range(2):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    squares.append(squ)

# 8. draw squares with color.
for idx, squ in enumerate(squares):
    squ.setFillColor(cols[idx])
    squ.setPos(pos[idx])
    squ.draw()
win.flip()
core.wait(2)
cue1s= []
##define element in cue1
for j in range(1):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    cue1s.append(squ)
for idx, squ in enumerate(cue1s):
    squ.setFillColor(colors[0])
    squ.setPos(pos1s[idx])
    squ.draw()
win.flip()
core.wait(Ts[0])
#res1
res1s= []
for k in range(1):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    res1s.append(squ)
for idx, squ in enumerate(res1s):
    squ.setFillColor(color1s[0])
    squ.setPos(pos1s[0])
    squ.draw()
t3 =core.getTime()
win.flip()
Ans1 = event.waitKeys(keyList = ['k','s'])
t4 =core.getTime()
block1s =[pos1s, Ts[0], Ans1] 
#cue2
cue2s= []
##define element in cue1
for l in range(1):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    cue2s.append(squ)
for idx, squ in enumerate(cue2s):
    squ.setFillColor(colors[0])
    squ.setPos(pos1s[idx+1])
    squ.draw()
win.flip()
core.wait(Ts[1])
#reps2
res2s= []
for k in range(1):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    res2s.append(squ)
for idx, squ in enumerate(res2s):
    squ.setFillColor(color1s[1])
    squ.setPos(pos1s[1])
    squ.draw()
win.flip()
t5 = core.getTime()
Ans2 = event.waitKeys(keyList = ['k','s'])
t6 = core.getTime()
RT = [t4-t3, t6-t5]

dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(2)}
print(dict1)
rv = dict(diff=[], same=[])

for idx, pos in enumerate(pos1s):
    key = ":".join(map(str, pos))
    if dict1[key] == color1s[idx]:
        rv['same'].append(key)
    else:
        rv['diff'].append(key)
        print(rv)
dataFile = open("%s.csv"%(info['cond']+'_'+info['sID']),'a')
dataFile.write(info['cond']+',' +info['setsize'] +',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + ',' +str(block1s) + ',' + str(rv) + ','+ str(RT) +'\n')
