def squBuilder(positions):
    squares=[]
    for pos in positions:
        squ = visual.Rect(WIN, lineColor="grey", size=[115, 115])
        squ.setPos(pos)
        squares.append(squ)
    return squares
def cir_build():
    circles=[]
    for pos in positions:
        cir = visual.Circle(WIN, radius = 40, edges = 50, lineWidth = 3, lineColor = 'white')
        cir.setPos(pos)
        circles.append(cir)
    return circles
def diam_biuld():
    diamonds=[]
    for pos in positions:
        diam = visual.Rect(WIN, lineColor='white', size=(165,165), ori =45, lineWidth =3 )
        diam.setPos(pos)
        diamonds.append(diam)
    return diamonds
def set():
    for i in range(4):
        positions = positions_builder(i)
        squares = square_builder(positions)
        positions_a = sample(positions, i/2)
        positions_b = set(positions)-set(positions_a)
        a_shape = a_diagram_builder(positions_a)
        b_shape = b_diagram_builder(positions_b)

#// first time
run(positions, positions_a, positions_b)
#// second time
run(positions, positions_a, positions_b)
'u' 
def positions_builder(i):
    positions_array=[]
    for i in range(4):
        positions_array.append(sample(POSITIONS,i))
    return positions_array

positions_builder()
def square_builder(positions=):
    for idx in positions_array:
        squBuilder()
        squares.setPos(positions_array[idx])
    #// 根據座標產生方形並回傳方形array
    return square_array
