from random import sample
import glob, os, sys, time
from psychopy import core, event, gui, visual, data, info
#####################background######################################


info = {'cond':['2000ms','1000ms'],'ID':'', 'age':'','gender':['Male','Female'], 'IntruC':['.3','2']}
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title = 'VisualWorkingMemory', 
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
    dataFile = open("%s.csv"%(info['cond']+'_'+info['sID']),'a')
    dataFile.write(info['cond']+',' +info['setsize'] +',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + ',' +str(block1s) + ',' + str(rv) + ','+ str(RT) +'\n')
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
    
    t = [.3, 2.0]
    Ts = sample(t,2)
    practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task. \nPress the "Space" key to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
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
    t2 = core.getTime()
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
    Ans1 = event.waitKeys(keyList = ['k','s'])
    Tk1 = core.getTime()
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
    Ans2 = event.waitKeys(keyList = ['k','s'])
    Tk2 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT1 = Tk1-t2
    RT2 = Tk2- Tk1
    block1s =[pos1s, Ts[0], Ans1, Ans2] 
    #cue2
    cue2s= []
    ##define element in cue1
    for l in range(2):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        cue2s.append(squ)
    for idx, squ in enumerate(cue2s):
        squ.setFillColor(colors[0])
        squ.setPos(pos1s[idx+2])
        squ.draw()
    win.flip()
    core.wait(Ts[1])
    t2 = core.getTime()
    #reps3
    res3s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res3s.append(squ)
    for idx, squ in enumerate(res3s):
        squ.setFillColor(color1s[2])
        squ.setPos(pos1s[2])
        squ.draw()
    win.flip()
    Ans3 = event.waitKeys(keyList = ['k','s'])
    Tk3 = core.getTime()
    #reps4
    res4s= []
    for k in range(1):
        squ = visual.Rect(win, lineColor="black", size=[100, 100])
        squ.draw()
        res4s.append(squ)
    for idx, squ in enumerate(res4s):
        squ.setFillColor(color1s[3])
        squ.setPos(pos1s[3])
        squ.draw()
    win.flip()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    Tk4 = core.getTime()
    
    RT3 = Tk3-t2
    RT4 = Tk4-Tk3
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos1s[2:], Ts[1], Ans3, Ans4]
    print(RT)
    print(block1s)
    print(block2s)
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(4)}
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
    dataFile.write(info['cond']+',' +info['setsize'] +',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')
    
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
    
    pos1s = sample(pos,2)
    pos2s = sample(pos,2)
    t = [.3, 2.0]
    Ts = sample(t,2)
    practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task. \nPress the "Space" key to start.',pos=(0,4),height= 30)
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
    t2 = core.getTime()
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
    Ans1 = event.waitKeys(keyList = ['k','s'])
    Tk1 = core.getTime()
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
    Ans2 = event.waitKeys(keyList = ['k','s'])
    Tk2 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT1 = Tk1-t2
    RT2 = Tk2- Tk1
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
    t2 = core.getTime()
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
    Ans3 = event.waitKeys(keyList = ['k','s'])
    Tk3 = core.getTime()
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
    Ans4 = event.waitKeys(keyList = ['k','s'])
    Tk4 = core.getTime()
    
    RT3 = Tk3-t2
    RT4 = Tk4-Tk3
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos2s, Ts[1], Ans3,Ans4]
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(6)}
    
    rv = dict(diff=[], same=[])
    
    for idx, pos in enumerate(pos1s + pos2s):
        key = ":".join(map(str, pos))
        if dict1[key] == color1s[idx]:
            rv['same'].append(key)
        else:
            rv['diff'].append(key)
    print(rv)
    
    dataFile = open("%s.csv"%(info['cond']+'_'+info['sID']),'a')
    dataFile.write(info['cond']+',' +info['setsize'] +',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')


def s8():
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
    practiceVWM = visual.TextStim(win=win,text='Get Read for VWM task. \nPress the "Space" key to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
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
    Ans1 = event.waitKeys(keyList = ['k','s'])
    Tk1 = core.getTime()
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
    Ans2 = event.waitKeys(keyList = ['k','s'])
    Tk2 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT2 = Tk2- Tk1
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
    t2 = core.getTime()
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
    Ans3 = event.waitKeys(keyList = ['k','s'])
    Tk3 = core.getTime()
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
    Ans4 = event.waitKeys(keyList = ['k','s'])
    Tk4 = core.getTime()
    
    ######################ExperimentHandler
    RT3 = Tk3-t2
    RT4 = Tk4-Tk3
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
    dataFile.write(info['cond']+',' +info['IntruC']+','+info['age']+','+info['gender']+ ',' + str(block2s) + ',' +str(block1s) + ',' + str(rv) + ',' + str(RT) +'\n')
