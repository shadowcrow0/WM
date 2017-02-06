from random import sample
import sys, time
from psychopy import core, event, gui, visual, data, info
#####################background######################################

info = {'cond':['2000ms','1000ms'],'ID':'', 'age':'','gender':['Male','Female']}
infoDlg = gui.DlgFromDict(dictionary = info, 
                          title = 'VWM Task', 
                          order = ['ID','cond','age'])
#if age != 0:
#    core.start()
#    else:
#        core.quit()
#### to do: check missing value ID, cond, age

if infoDlg.OK == False:
    core.quit()
#######s2()
def s2468():
    win = visual.Window([800,600],color = "black", units = 'pix')
    practiceVWM = visual.TextStim(win=win,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    practiceVWM.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
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
    block1s = [Ts[0], Ans1, Ts[1], Ans2]
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
    with open("%s_%s_%s.csv" % (info['cond'], info['ID'], setsize),'a') as f:
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        setsize,
        info['cond'], info['ID'], info['age'], info['gender'],
        block1s, 
        rv['diff'], rv['same'],RT))
#################set2END##############set4START###########################
    # 1. define 4 Colors
    colors = ['white','#FF0000', '#FFA500', '#0000FF', '#2AA54C']
    #1.1 define color appear in response trial
    cols = sample(colors[1:],4)
    color1s = sample(colors[1:], 4)
    # 2. define 4 positions.
    pos = [
        [-100,100], 
        [100,100], 
        [-100,-100], 
        [100,-100]
        ]
    pos1s = sample(pos,4)
    t = [.3, 2.0]
    Ts = sample(t,2)
    #Start drawing stim
    next = visual.TextStim(win=win,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
    fix.draw()
    win.flip()
    core.wait(.5)
    t1 = core.getTime()
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
    VWM4_1 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM4_1.draw()
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
    VWM4_2 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM4_2.draw()
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
    VWM4_3 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM4_3.draw()
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
    VWM4_4 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM4_4.draw()
    win.flip()
    t7 = core.getTime()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    t8 = core.getTime()
    RT4 = t8-t7
    RT = [RT1, RT2, RT3, RT4]
    block2s = [pos2s, Ts[1], Ans3, Ans4]
    dict1 = {":".join(map(str, pos[idx])): cols[idx] for idx in range(4)}
    print(dict1)
    
    rv = dict(diff=[], same=[])
    setsize = 4
    for idx, pos in enumerate(pos1s):
        key = ":".join(map(str, pos))
        if dict1[key] == color1s[idx]:
            rv['same'].append(key)
        else:
            rv['diff'].append(key)
            print(rv)
    with open("%s_%s_%s.csv" % (info['cond'], info['ID'], setsize),'a') as f:
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        setsize,
        info['cond'], info['ID'], info['age'], info['gender'],
        block1s, block2s,
        rv['diff'], rv['same'],
        RT))
        ########################set4END###############set6START#######################
    win = visual.Window([800,600],color = "black", units = 'pix')
    next = visual.TextStim(win=win,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
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
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
    fix.draw()
    win.flip()
    core.wait(.5)
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
    VWM6_1 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM6_1.draw()
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
    VWM6_2 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM6_2.draw()
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
    VWM6_3 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM6_3.draw()
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
    VWM6_4 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,200])
    VWM6_4.draw()
    win.flip()
    t7 = core.getTime()
    Ans4 = event.waitKeys(keyList = ['k','s'])
    t8 = core.getTime()
    RT4 = t8-t7
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
    with open("%s_%s_%s.csv" % (info['cond'], info['ID'], setsize),'a') as f:
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        setsize,
        info['cond'], info['ID'], info['age'], info['gender'],
        block1s, block2s,
        rv['diff'], rv['same'],
        RT))    
    ###################set6END###################set8START############################
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
    next = visual.TextStim(win=win,text='Get Ready for VWM task. Remember color and position, \nPress "Space" to start.',pos=(0,4),height= 30)
    next.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    core.wait(.3)
    fix = visual.TextStim(win,text='+', height=40, color='white',pos=[0,0])
    fix.draw()
    win.flip()    
    core.wait(.5)
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
    VWM8_1 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,250])
    VWM8_1.draw()
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
    VWM8_2 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,250])
    VWM8_2.draw()
    win.flip()
    t3 = core.getTime()
    Ans2 = event.waitKeys(keyList = ['k','s'])
    t4 = core.getTime()
    #creat dic1 and dic2 compare if position value
    RT2 = t4-t3
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
    VWM8_3 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,250])
    VWM8_3.draw()
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
    VWM8_4 = visual.TextStim(win=win,text='If color is same, press "S" \nIf color is different,press"K" ',height= 20, pos = [0,250])
    VWM8_4.draw()
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
    with open("%s_%s_%s.csv" % (info['cond'], info['ID'], setsize),'a') as f:
        f.write("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
        setsize,
        info['cond'], info['ID'], info['age'], info['gender'],
        block1s, block2s,
        rv['diff'], rv['same'],
        RT))
        #############SET8END################################

