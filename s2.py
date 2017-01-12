import time
import sys
from psychopy import visual,event,core
import random

t0 = core.getTime()

win = visual.Window([800,600],color="black", units='pix')
fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
fix.draw()
win.flip()
core.wait(.5)
t1 = core.getTime()

square1 = visual.Rect(win,lineColor="black",size=[100,100])
square2 = visual.Rect(win,lineColor="black",size=[100,100])

col = ['#FF0000', '#FFA500'] #, '#0000FF', '#2AA54C','#7D3A4B']

location = [[-100,100], [100,100]]#, [-100,-100], [100,-100]]
color = random.sample(col, 2)

time = [.3 , 2.0, .3, 2.0, .3, 2.0, .3, 2.0]
t = random.sample(time, 2)
color1 = random.sample(col, 2)
location1 = random.sample(location, 2)


square1.setPos(location[0])
square1.setFillColor(color[0])
square2.setPos(location[1])
square2.setFillColor(color[1])

square1.draw()
square2.draw()
win.flip()
core.wait(2.0)
t2 = core.getTime()
###block1#####
cue1 = visual.Rect(win,lineColor="black",size=[100,100])
cue1.setFillColor('white')
cue1.setPos(location1[0])
cue1.draw()
win.flip()
core.wait(t[0])
t3 = core.getTime()# should be equal to t[0]


res1 = visual.Rect(win,lineColor="black",size=[100,100])
res1.setFillColor(color1[0])
res1.setPos(location1[0])
res1.draw()
win.flip()
resp1 = event.waitKeys(keyList = ['k','s'])
t4 = core.getTime()

###block2#####
cue2 = visual.Rect(win,lineColor="black",size=[100,100])
cue2.setFillColor('white')
cue2.setPos(location1[1])
cue2.draw()
win.flip()
core.wait(t[1])
t5 = core.getTime()# should be equal to t[1]

res2 = visual.Rect(win,lineColor="black",size=[100,100])
res2.setFillColor(color1[1])
res2.setPos(location1[1])
res2.draw()
win.flip()
resp2 = event.waitKeys(keyList = ['k','s'])
t6 = core.getTime()
########data################
#c = random.choice(col)
#print(c)
IC = [t[0], t[1]]
print("IntrsuionCost =")
print(IC)
###about blocka1
print("1st cue apear in")
print(t[0])
print("1st block should be")
print(color1[0])
print(color1[1])
print("this stimul=>")
print(color)
print(location)
print("1st block appear in ")
print(location1[0])
print(location1[1])
print(resp1)
print(resp2)
#####about block2
print("2nd cue apear in")
print(t[1])
print("this stimul show in")
print(location)
print("2nd block cues apear")
print("this stimul=>")
print(color)
print("2nd block should be")
RT = [t4, t6]
print(RT)
