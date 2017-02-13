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
# 1.1 all colors in use
allColors = ['white','#FFDA00', '#52FFAE', '#3E0DE4', '#F8E214', '#CDF118', '#A52A2A', '#1118BB', '#6C3EFF']
 
# 1.2 sample colors for experiment
a = sample(allColors[1:],8) #setsize8
a_4 = sample(a,4)
b = sample(allColors[1:],6) #setsize6
b_4 = sample(b,4)
c = sample(allColors[1:],4) #setsize4
c_4 = sample(c,4)
d = sample(allColors[1:],2) #setsize2
d_2 = sample(d,2)
# 2.1 all pos in use
pos2 = [[-100,100],[100,100] ]
pos4 = [[-100,100], 
        [100,100], 
        [-100,-100], 
        [100,-100]]
pos6 = [
        [100,100], 
        [-100,100], 
        [-150,0], 
        [150,0],
        [-100,-100],
        [100,-100]
]
pos8 = [
        [-100, 200],
        [-200, 100],
        [-200, -100],
        [-100, -200],
        [100, -200],
        [200, -100],
        [200, 100],
        [100, 200]
]


#2.2 sample pos in cue
w_2 = sample(pos2,2)
x_4 = sample(pos4,4)
y_6 = sample(pos6,4)
z_8 = sample(pos8,4)

#2.3 make list of sample for pos
#posList1 = {"w_2":w_2,"x_4": x_4,"y_6":y_6, "z_8":z_8}
#print(posList1) 
posList2 = [w_2, x_4, y_6, z_8]
#print "dict: {}, \n\nlist: {}".format(posList1,posList2)

ra = {str(pos8):a}
dict1 = {":".join(map(str, pos8[idx])): a[idx] for idx in range(8)}
print(dict1)
rv = dict(diff=[], same=[])
for idx, z_8 in enumerate(z_8):
    key = ":".join(map(str, z_8))
    if ra[key] == z_8[idx]:
        rv['same'].append(key)
    else:
        rv['diff'].append(key)
        print(rv)
#3.1 IC
Ts = sample([.3,2],2)
