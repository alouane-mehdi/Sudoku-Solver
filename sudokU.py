import numpy as np
with open("t.txt") as my_file:
    tabl =[]
    tabl = my_file.read()
tabl1 = []
t=0
tabl2=[]
for i in tabl:
    if i!= '\n' :
        tabl1.append(i)
for i in range (0,9):
    tabl2.append(tabl1[0:9])
    del tabl1[0:9]

for i in tabl2:
    if  i !='_':
        print(i)
    