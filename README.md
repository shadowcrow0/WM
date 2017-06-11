#python 27  #psychopy

#experiment 1 VWM task.**

random assign positions to circle and diamond.

 1.setsize = 1,2,3,4 per circle and diamond.
 
 min 2 squares with circle and diamond
 
 max 8 squares with 4 circles and 4 diamonds
 
 2.Probe Type:0(positive), 1(new), 2(intrusion)
 
 half probes are assigned to positive, quater probes for intrusion, quater for new.
 
 countanbanlancing false alarm rate.
  
  3.CSI(cue-stimuli interval):0.3/2.0s

  4.1 DV: RT and correctness
  
  4.2 within subjects design
  
  4.3 Total trials: 480
  
  4.4 80 trials per block.
  
  5.Each trial include
      learning list (2s)
      1st cue(.3/2s)
      1st Probe
      Feedback(1.5s)
      2nd cue(.3/2s)
      2nd Probe
      Feedback(1.5s)
  

#experiment 2 VWM task.**


  1.fixed cue frame: seperate screen to upside and down.

  2.IV:ProbeType(3), CSI(3), Setsize(4)
  
  2.1 Probe Type:0(positive), 1(new), 2(intrusion)
  
  
   half probes are assigned to positive, quater probes for intrusion, quater for new, 
   
   
   in order to countanbanlancing false alarm rate.
      
  2.2.CSI(cue-stimuli interval):0.3/2.0s/5s
  
  2.3 setsize :1~4 for circle and diamond
               2,4,6,8 for sqaures
               
  3.Procedure
  
# For exp2, you might need

1.vwm2.py

2.csvtest.py

3.setstim.py

4.IV.csv

5.vwm.csv

##optional##

If you can't build enviromnent on psychopy, download lib and venv
