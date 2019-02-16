import string

fisierin = open("lvl1-0.inp", "r")
newfeld = []
nrimg = 0
for line in fisierin:
    fiels = line.strip('\n')
    newfeld.append(fiels.split(" "))
Images = int(newfeld[0][2])
valueCnt = 0
while(Images):
    leng = int(newfeld[nrimg + 1][1])  
    for i in range(int(newfeld[0][2])):
        for j in range(len(newfeld[i])):
            if newfeld[i + leng][j] > 0:
                valueCnt += 1
    if valueCnt > 0:
            print newfeld[1][0]
    leng += int(newfeld[nrimg])
    Images -= 1
    nrimg += 1
    valueCnt = 0