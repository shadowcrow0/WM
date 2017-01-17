from random import sample
import time
import sys
from psychopy import core, event, gui, visual, data
#####################background######################################
win = visual.Window([800,600],color = "black", units = 'pix')
# 1. define 8 Colors
colors = ['white','red', 'orange', 'blue', 'yellow', 'green', 'brown', 'pink', 'purple']
#1.1 define color appear in response trial

color1s = sample(colors[1:], 4)
# 2. define 8 positions.
pos = [
    [-100, 200],
    [-200, 100],
    [-200, -100],
    [-100, -200],
    [100, -200],
    [200, -100],
    [200, 100],
    [100, 200]
]


pos1s = sample(pos,2)
print(pos1s)
pos2s = sample(pos,2)
print(pos2s)

practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task. \nPress the "Space" key to start.',pos=(0,4),height= 30)
practiceVWM.draw()
win.flip()
event.waitKeys(keyList = 'space')
fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
fix.draw()
core.wait(.5)
win.flip()
t1 = core.getTime()

# 7. draw shape and wait 2000ms
squares = []
for i in range(8):
    squ = visual.Rect(win, lineColor="black", size=[100, 100])
    squ.draw()
    squares.append(squ)

# 8. draw squares with color.
for idx, squ in enumerate(squares):
    squ.setFillColor(colors[idx+1])
    squ.setPos(pos[idx])
    squ.draw()
core.wait(2)
win.flip()
# 9. cue1
def cue():
    cues= []
    for x in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cues.append(squ)
    for idx, squ in enumerate(cues):
        squ.setFillColor(colors[0])
        squ.setPos(pos1s[idx])
        squ.draw()
    t = [.3, 2.0]
    Ts = sample(t,2)
    win.flip()
    core.wait(Ts[0])
    print(Ts[0])
#10 cue 2 
def cue2():
    cue2s= []
    for y in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cue2s.append(squ)
    for idx, squ in enumerate(cue2s):
        squ.setFillColor(colors[0])
        squ.setPos(pos2s([idx])
        squ.draw()
    win.flip()
def res():
    res= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res.append(squ)
    for idx, squ in enumerate(res):
        squ.setFillColor(color1s[0])
        print(color1s)
        squ.setPos(pos1s[0])
        squ.draw()
    win.flip()
    Ans = event.waitKeys(keyList = ['k','s'])
    Tk = core.getTime()
    print(Tk)
    print(Ans)







def res2s():
    res2s= []
    for l in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res2s.append(squ)
        print(color1s[1])
    for idx, squ in enumerate(res2s):
        squ.setFillColor(color1s[1])
        squ.setPos(pos1s[1])
        squ.draw()
        
    win.flip()
    Ans = event.waitKeys(keyList = ['k','s'])
    Tk = core.getTime()
    print(Tk)
    print(Ans)

cue()
res()
res2s()
cue()
res()
res2s()
