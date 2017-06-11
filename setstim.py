col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []#down 4 position
colors =[]
col_as =[]# col_a -> top 4 squares
color = []
col_bs = []#col_b -> down 4 squares
upss = []#top 4 positions
poss = []#all position
downss = []#down 4 position

import csv
import  ast
with open('vwm2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        colors.append(row['color'])
        col_as.append(row['col_a'])
        col_bs.append(row['col_b'])
        poss.append(row['pos'])
        upss.append(row['ups'])
        downss.append(row['downs'])
    for i in colors:
        color.append(ast.literal_eval(i))
     #   print  repr(color)
    for i in col_bs:
        col_b.append(ast.literal_eval(i))
    #    print len(col_b)
    for i in poss:
        pos.append(ast.literal_eval(i))
   #     print len(pos)
    for i in col_as:
        col_a.append(ast.literal_eval(i))
  #      print len(col_a)
    for i in upss:
        ups.append(ast.literal_eval(i))
 #       print len(ups)
    for i in downss:
        downs.append(ast.literal_eval(i))
#        print  len(downs)
