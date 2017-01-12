import random
import time
import sys
from psychopy import visual,core,event,data,gui
from psychopy.tools.filetools import fromFile,toFile

#phase = visual.TextStim(win=win,height= 30, color= 'white',text='This is the practice phase. \nWhen you are ready, please press the "Space" key to continue.')
#practiceVWM = visual.TextStim(win=win,text='Practice block of VWM task. \nPress the "Space" key to continue.',pos=(0,4),height= 30)

#setting
win = visual.Window(monitor='testMonitor',color="black", units='pix',fullscr = False)

t0 = core.getTime()
