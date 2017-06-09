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

import pyexcel as pe
records = pe.iget_records(file_name="IV.ods")
for record in records:
    sz.append(record['sz'])
    CSIs.append(record['CSI'])
    cat1.append(record['cat1'])
    ProbeTypes.append(record['ProbeType'])
    CSI2s.append(record['CSI2'])
    cat2.append(record['cat2'])
    thisN.append(record['trial'])
    thisIndex.append(record['position'])
    ProbeType2s.append(record['ProbeType2'])
#    print ('sz ={} ,CSI= {},'.format(record['sz'],record['CSI']))
recor = pe.iget_records(file_name="vwm.ods")
for record in recor:
    color.append(record['color'])
    col_a.append(record['col_a'])
    col_b.append(record['col_b'])
    pos.append(record['pos'])
    ups.append(record['ups'])
    downs.append(record['downs'])
    print ('color = {} at pos: {}'.format(record['color'],record['pos']))