from library import *

col = {"party":12, "fgm":5, "fga":4, "RidingNumber":2}
data = loadList("RidingWinners.csv")
LiberalCount = 0
NDPCount = 0
ConservativeCount = 0
BQCount = 0
GreenCount = 0
LiberalList = []
NDPList = []
ConservativeList = []
BQList = []
GreenList = []
RidingCountList = []

for n in range (0,len(data)):
    if data[n][col["party"]][-1] == 'l':
        LiberalCount += 1
        LiberalList.append(data[n][col["RidingNumber"]])
    elif data[n][col["party"]][-1] == 'e':
        NDPCount += 1
        NDPList.append(data[n][col["RidingNumber"]])
    elif data[n][col["party"]][-1] == 'r':
        ConservativeCount += 1
        ConservativeList.append(data[n][col["RidingNumber"]])
    elif data[n][col["party"]][-1] == 's':
        BQCount += 1
        BQList.append(data[n][col["RidingNumber"]])
    else:
        GreenCount += 1
        GreenList.append(data[n][col["RidingNumber"]])


print(LiberalList)
print(ConservativeList)
print(NDPList)
print(BQList)
print(GreenList)



