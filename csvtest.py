import csv
sz = []#setsize, determine how many squares need to present
ProbeType2s = []
CSI2s = []
ProbeTypes = []
CSIs = []
cue = []
thisN = []
thisIndex = []
col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []#down 4 position
cat1 =[]
cat2 = []
cue_order = []
FEEDBACK = []
with open('IV.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sz.append(int(row['sz']))
        CSIs.append(float(row['CSI']))
        CSI2s.append(float(row['CSI2']))
        ProbeTypes.append(int(row['ProbeType']))
        ProbeType2s.append(int(row['ProbeType2']))
        cat1.append(int(row['cat1']))
        cat2.append(int(row['cat2']))
        cue_order.append(int(row['cueorder']))
        #pos.append(row['pos'])
        #color.append(''.join(row['color']))
        #ups.append(row['ups'])
        #downs.append(row['downs'])
        #col_a.append(row['col_a'])
        #col_b.append(row['col_b'])
        thisIndex.append(row['position'])
        thisN.append(row['trial'])
#print  sz