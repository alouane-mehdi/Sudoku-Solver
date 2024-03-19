import numpy as np

with open("t.txt") as my_file:
    tabl = my_file.read()

tabl1 = []
for i in tabl:
    if i != '\n':
        tabl1.append(i)

tabl2 = []
for i in range(0, 9):
    tabl2.append(tabl1[0:9])
    del tabl1[0:9]

for i in range(len(tabl2)):
    for j in range(len(tabl2[i])):
        if tabl2[i][j] == '_':
            tabl2[i][j] = '1'

for row in tabl2:
    print(row)
