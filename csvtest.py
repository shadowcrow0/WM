import csv
sz = []#setsize, determine how many squares need to present
ProbeType2s = []
CSI2s = []
ProbeTypes = []
CSIs = []
cue = []
thisN = []
thisIndex = []
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
        thisIndex.append(row['position'])
        thisN.append(row['trial'])
