col_a =[]# col_a -> top 4 squares
color = []
col_b = []#col_b -> down 4 squares
ups = []#top 4 positions
pos = []#all position
downs = []#down 4 position
import csv
import  ast
with open('vwm2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        color.append(row['color'])
        col_a.append(row['col_a'])
        col_b.append(row['col_b'])
        pos.append(row['pos'])
        ups.append(row['ups'])
        downs.append(row['downs'])
for i in color:
    color = ast.literal_eval(i)
for i in col_b:
    col_b = ast.literal_eval(i)
for i in pos:
    pos = ast.literal_eval(i)
for i in col_a:
    col_a = ast.literal_eval(i)
for i in ups:
    ups = ast.literal_eval(i)
for i in downs:
    downs = ast.literal_eval(i)
