from random import sample,shuffle

COLORS = ['#ffb6c1', '#deb887', '#ff8000', '#800080', '#00e673', '#008080', '#ff8c00', '#006666','#006400','#6B8E23','#8b4513']
POSITIONS = [(-200, 100), (-100, 200), (100, 200), (200, 100), (100, -200), (200, -100), (-200, -100), (-100, -200)]
col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []
col_new = []
a = POSITIONS[0:4]
b = POSITIONS[4:8]


sz = shuffle(range(4))
def giveColPos(sz):
    for i in sz:
        color = sample(COLORS, 2*sz)
        col_a = color[0:sz]
        col_b = color[sz:]
        col_new = sample(list(set(COLORS) - set(color)), 1)[0]
        pos = sample(POSITIONS, sz)
        ups = sample(a, sz)
        downs = sample(b, sz)
    return col_new, color, pos, ups, downs, col_b, col_a
def choseType():
    for i in range(4):
        if i % 2 !=0: #asign Probetype
            ProbeType = 0
        elif i % 4 == 2:
            ProbeType = 2
        elif i % 4 ==0:
            ProbeType = 1
    return ProbeType


def getProbeColor(ProbeType):
    col_positive = []
    col_intrusion = []
    display_color = []
    if cue == 1:  # diamond circle
        col_positive = sample(col_b,1)[0]
        col_intrusion = sample(col_a,1)[0]
        if col_intrusion == col_positive:
            col_intrusion = sample(col_a,1)[0]
    elif cue == 0:  # circle diamond
        col_positive = sample(col_a,1)[0]
        col_intrusion = sample(col_b,1)[0]
        if col_intrusion == col_positive:
            col_intrusion = sample(col_b,1)[0]
    if ProbeType == 0:
        display_color = col_positive
    elif ProbeType == 1:
        display_color = col_intrusion
    elif ProbeType == 2:
        display_color = col_new
    return display_color
def setup():
    global sz
    cue = sample([0, 1], 2)
    (color, col_new, ups, downs, col_b, col_a) = giveColPos(sz)
    CSI1 = sample([.3,2,5],1)[0]
    cue = cue[0]
    display_color = getProbeColor()
    ProbeType1 = choseType()
    CSI2 = sample([.3,2,5],1)[0]
    cue = cue[1]
    ProbeType2 = choseType()
    display_color2 = getProbeColor()
    return display_color, cue, CSI2, CSI1, sz, ProbeType1, ProbeType2,display_color,display_color2



def save_resp(color, col_new, ups, downs,sz):
    (display_color, cue, CSI2, CSI1, sz, ProbeType1, ProbeType2, display_color, display_color2) = setup()
    dataFile = open('setting.csv', 'a')
    color = str(color)
    col_new = str(col_new)
    ups = str(ups)
    downs = str(downs)
    sz =str(sz)
    dataFile.write(sz +',' + col_new +','+thisidx+','+ CSI1 +',' +ProbeType1 +','+cue[0]+','+display_color+','+ProbeType2 +',' +CSI2+','+display_color2+','+cue[1]+ color +','+ ups +','+ downs + '\n')


for thisidx in range(16):
    giveColPos()
    choseType()
    setup()
    save_resp(color, col_new, ups, downs,sz)
