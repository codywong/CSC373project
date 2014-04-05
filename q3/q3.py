from numpy  import *
import sys
import math
file = open('q3_medium.dat') #sys.stdin


def calculateCost(colS, colT):
    pos = 0
    cost = 0
    sHeight = len(colS)
    while (pos != sHeight):
        if (colS[pos] == '-' or colT[pos] == '-'):
            break
        passMatches = 0
        swapMatches = 0
        removeMatches = 0
        
        # calculate the number of matches of boxes above current position
        # if you swap or pass(don't do anything)
        for examine_pos in range(pos, sHeight):
            # if first/bottom of currently examined start point
            if examine_pos==pos:
                if colS[examine_pos] == colT[examine_pos]:
                    passMatches += 1
                else: # bottom two are not the same letter boxes
                    swapMatches +=1
            elif colS[examine_pos] == colT[examine_pos]:
                swapMatches += 1
                passMatches += 1
    
        # calculate number of matches if you removed a box
        for examine_pos in range(pos+1, sHeight):
            if colS[examine_pos] == colT[examine_pos-1]:
                removeMatches += 1
                
        # select the move with the most benefit
        if max(passMatches, swapMatches, removeMatches) == passMatches:
            pos += 1
        # if swap is tied with remove
        elif (swapMatches == removeMatches):
            boxes_in_s = len(colS) - colS.count('-')
            boxes_in_t = len(colT) - colT.count('-')
            # s has more boxes than t, better to remove
            if boxes_in_s > boxes_in_t:
                cost += 1
                sHeight -= 1
                colS.pop(pos)
            else:
                pos += 1
                cost += 1                        
        # if remove is better
        elif max(passMatches, swapMatches, removeMatches) == swapMatches:
            pos += 1
            cost += 1
        #remove is better
        else:
            cost += 1
            sHeight -= 1
            colS.pop(pos)
        
    cost += math.fabs((len(colT) - len(colS) + colS.count('-')) - colT.count('-'))
    return cost;

#convert input array as [time@ground, position]
m = 1
n = 1
linenumber = 0

while (True):
    line = file.readline()
    if line[:1] != '#':
        m = int(line.strip())
        break
    
n = int(file.readline().strip())

S_temp = []
for x in range(m):
    row = file.readline().strip().split(' ')
    S_temp.append(row)

T_temp = []    
for x in range(m):
    row = file.readline().strip().split(' ')
    T_temp.append(row)

S = []
T = []
#swap columns and rows of S and T
for i in range(n):
    S.append([])
    T.append([])
    for j in range(m-1, -1 ,-1):
        S[i].append(S_temp[j][i])
        T[i].append(T_temp[j][i])
        

total = 0
for i in range(0, n):
    a = calculateCost(S[i], T[i])
    print(str(int(a)))
    total += a

print('Total  ' + str(int(total)))