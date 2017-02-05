# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:05:40 2017

@author: root
"""

from random import sample
import sys, time
from psychopy import core, event, gui, visual, data, info
#####################background######################################

info = {'cond':['2000ms','1000ms'],'ID':'', 'age':'','gender':['Male','Female']}
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title = 'VWM Task', 
                          order = ['ID','cond','age'])
if infoDlg.OK == False:
    core.quit()

def s2():
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
    setsize = 2
    t = [.3, 2.0]
    Ts = sample(t,2)
    practiceVWM = visual.TextStim(win=win,text='Get Ready for VWM task. \nRemember color and position,\nPress the "Space" key to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    fix = visual.TextStim(win,text='+', height=80, color='white',pos=[0,0])
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
    VWM1 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM1.draw()
    win.flip()
    Ans1 = event.waitKeys(keyList = ['k','s'])
    t4 =core.getTime()
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
    VWM2 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM2.draw()
    win.flip()
    t5 = core.getTime()
    Ans2 = event.waitKeys(keyList = ['k','s'])
    t6 = core.getTime()
    RT = [t4-t3, t6-t5]
    block1s = [Ts[0], Ans1, RT[0], Ts[1], Ans2, RT[1]]
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
    dataFile = open("%s.csv"%(info['cond']+'_'+info['ID']),'a')
    dataFile.write(info['cond']+',' + info['ID'] + ',' + info['age']+','+info['gender']+ ',' + ',' +str(block1s) + ',' + str(rv) + ','+ str(RT) +'\n')
def s4():
    win = visual.Window([800,600],color = "black", units = 'pix')
    # 1. define 4 Colors
    colors = ['white','#FF0000', '#FFA500', '#0000FF', '#2AA54C']
    #1.1 define color appear in response trial
    cols = sample(colors[1:],4)
    color1s = sample(colors[1:], 4)
    # 2. define 8 positions.
    pos = [
        [-100,100], 
        [100,100], 
        [-100,-100], 
        [100,-100]
        ]
    
    pos1s = sample(pos,4)
    setsize = 4
    t = [.3, 2.0]
    Ts = sample(t,2)
    practiceVWM = visual.TextStim(win=win,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    fix = visual.TextStim(win,text='+', height=80, color='white',pos=[0,0])
    fix.draw()
    core.wait(.5)
    win.flip()    
    # 7. draw shape and wait 2000ms
    squares = []
    for i in range(4):
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
    for j in range(2):
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
    win.flip()
    t1 = core.getTime()
    Ans1 = event.waitKeys(keyList = ['k','s'])
    t2 = core.getTime()
    RT1 = t2-t1   
    #res2
    res2s= []
    for m in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res2s.append(squ)
    for idx, squ in enumerate(res2s):
        squ.setFillColor(color1s[1])
        squ.setPos(pos1s[1])
        squ.draw()
    win.flip()
    t3 = core.getTime()
    Ans2 = event.waitKeys(keyList = ['k','s'])
    t4 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT2 = t4-t3
    block1s =[pos1s, Ts[0], Ans1, Ans2] 
    pos2s = sample(pos,2)
    #cue2
    cue2s= []
    ##define element in cue1
    for l in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cue2s.append(squ)
    for idx, squ in enumerate(cue2s):
        squ.setFillColor(colors[0])
        squ.setPos(pos2s[idx])
        squ.draw()
    win.flip()
    core.wait(Ts[1])
    #reps3
    res3s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res3s.append(squ)
    for idx, squ in enumerate(res3s):
        squ.setFillColor(color1s[2])
        squ.setPos(pos2s[0])
        squ.draw()
    win.flip()
    t5 = core.getTime()
    Ans3 = event.waitKeys(keyList = ['k','s'])
    t6 = core.getTime()
    RT3 = t5 - t6
    #reps4
    res4s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res4s.append(squ)
    for idx, squ in enumerate(res4s):
        squ.setFillColor(color1s[3])
        squ.setPos(pos2s[1])
        squ.draw()
    win.flip()
    t7 = core.getTime()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    t8 = core.getTime()
    RT4 = t8-t7
    ######################ExperimentHandler
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos2s, Ts[1], Ans3,Ans4]
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in len(cols)}
    print(dict1)
    rv = dict(diff=[], same=[])
    
    for idx, pos in enumerate(pos1s + pos2s):
        key = ":".join(map(str, pos))
        if dict1[key] == color1s[idx]:
            rv['same'].append(key)
        else:
            rv['diff'].append(key)
    print(rv)
    dataFile = open("%s.csv"%(info['cond']+'_'+info['ID']),'a')
    dataFile.write(str(setsize)+ ',' +info['cond']+',' +info['ID']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')
def s6():
    #####################background######################################
    win = visual.Window([800,600],color = "black", units = 'pix')
    # 1. define 6 Colors
    colors = ['white', '#FFA500', '#0000FF', '#2AA54C','#D1FF00','#394A83','#7D3A4B']
    #1.1 define color appear in response trial
    cols = sample(colors[1:],6)
    color1s = sample(colors[1:], 4)
    # 2. define 6 positions.
    pos = [
        [100,100], 
        [-100,100], 
        [-150,0], 
        [150,0],
        [-100,-100],
        [100,-100]
        ]
    setsize = 6
    pos1s = sample(pos,2)
    pos2s = sample(pos,2)
    t = [.3, 2.0]
    Ts = sample(t,2)
    practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task./n Remember color and position /n Press the "Space" key to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
    fix.draw()
    core.wait(.5)
    win.flip()
 
    # 7. draw shape and wait 2000ms
    squares = []
    for i in range(6):
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
    for j in range(2):
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
    win.flip()
    t1 = core.getTime()
    Ans1 = event.waitKeys(keyList = ['k','s'])
    t2 = core.getTime()
    RT1 = t2-t1   
    #res2
    res2s= []
    for m in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res2s.append(squ)
    for idx, squ in enumerate(res2s):
        squ.setFillColor(color1s[1])
        squ.setPos(pos1s[1])
        squ.draw()
    win.flip()
    t3 = core.getTime()
    Ans2 = event.waitKeys(keyList = ['k','s'])
    t4 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT2 = t4-t3
    block1s =[pos1s, Ts[0], Ans1, Ans2] 
    pos2s = sample(pos,2)
    #cue2
    cue2s= []
    ##define element in cue1
    for l in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cue2s.append(squ)
    for idx, squ in enumerate(cue2s):
        squ.setFillColor(colors[0])
        squ.setPos(pos2s[idx])
        squ.draw()
    win.flip()
    core.wait(Ts[1])
    #reps3
    res3s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res3s.append(squ)
    for idx, squ in enumerate(res3s):
        squ.setFillColor(color1s[2])
        squ.setPos(pos2s[0])
        squ.draw()
    win.flip()
    t5 = core.getTime()
    Ans3 = event.waitKeys(keyList = ['k','s'])
    t6 = core.getTime()
    RT3 = t5 - t6
    #reps4
    res4s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res4s.append(squ)
    for idx, squ in enumerate(res4s):
        squ.setFillColor(color1s[3])
        squ.setPos(pos2s[1])
        squ.draw()
    win.flip()
    t7 = core.getTime()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    t8 = core.getTime()
    RT4 = t8-t7
    ######################ExperimentHandler
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos2s, Ts[1], Ans3,Ans4]
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(6)}
    print(dict1)
    
    rv = dict(diff=[], same=[])
    
    for idx, pos in enumerate(pos1s + pos2s):
        key = ":".join(map(str, pos))
        if dict1[key] == color1s[idx]:
            rv['same'].append(key)
        else:
            rv['diff'].append(key)
    print(rv)
    dataFile = open("%s.csv"%(info['cond']+'_'+info['ID']),'a')
    dataFile.write(str(setsize)+ ',' +info['cond']+',' +info['ID']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')

def s8():
    setsize = 8
    win = visual.Window([800,600],color = "black", units = 'pix')
    # 1. define 8 Colors
    colors = ['white','red', 'orange', 'blue', 'yellow', 'green', 'brown', 'pink', 'purple']
    #1.1 define color appear in response trial
    cols = sample(colors[1:],8)
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
    pos2s = sample(pos,2)
    t = [.3, 2.0]
    Ts = sample(t,2)
    
    ########################stimul##########################
    practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task./n Press the "Space" key to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    intro =  visual.TextStim(win, text = 'Remember color and position', height = 30, color = 'white',pos = [0,250])
    intro.draw()
    win.flip()
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
    fix.draw()
    core.wait(.5)
    win.flip()    
    # 7. draw shape and wait 2000ms
    squares = []
    for i in range(8):
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
    for j in range(2):
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
    win.flip()
    t1 = core.getTime()
    Ans1 = event.waitKeys(keyList = ['k','s'])
    t2 = core.getTime()
    RT1 = t2-t1   
    #res2
    res2s= []
    for m in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res2s.append(squ)
    for idx, squ in enumerate(res2s):
        squ.setFillColor(color1s[1])
        squ.setPos(pos1s[1])
        squ.draw()
    win.flip()
    t3 = core.getTime()
    Ans2 = event.waitKeys(keyList = ['k','s'])
    t4 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT2 = t4-t3
    block1s =[pos1s, Ts[0], Ans1, Ans2] 
    pos2s = sample(pos,2)
    #cue2
    cue2s= []
    ##define element in cue1
    for l in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cue2s.append(squ)
    for idx, squ in enumerate(cue2s):
        squ.setFillColor(colors[0])
        squ.setPos(pos2s[idx])
        squ.draw()
    win.flip()
    core.wait(Ts[1])
    #reps3
    res3s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res3s.append(squ)
    for idx, squ in enumerate(res3s):
        squ.setFillColor(color1s[2])
        squ.setPos(pos2s[0])
        squ.draw()
    win.flip()
    t5 = core.getTime()
    Ans3 = event.waitKeys(keyList = ['k','s'])
    t6 = core.getTime()
    RT3 = t5 - t6
    #reps4
    res4s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res4s.append(squ)
    for idx, squ in enumerate(res4s):
        squ.setFillColor(color1s[3])
        squ.setPos(pos2s[1])
        squ.draw()
    win.flip()
    t7 = core.getTime()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    t8 = core.getTime()
    RT4 = t8-t7
    ######################ExperimentHandler
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos2s, Ts[1], Ans3,Ans4]
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(8)}
    print(dict1)
    
    rv = dict(diff=[], same=[])
    
    for idx, pos in enumerate(pos1s + pos2s):
        key = ":".join(map(str, pos))
        if dict1[key] == color1s[idx]:
            rv['same'].append(key)
        else:
            rv['diff'].append(key)
    print(rv)
    dataFile = open("%s.csv"%(info['cond']+'_'+info['ID']),'a')
    dataFile.write(str(setsize)+ ',' +info['cond']+',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')

#s2()
#s4()
#s6()
#s8()
