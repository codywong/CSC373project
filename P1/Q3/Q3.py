import sys
import math
file = sys.stdin


def calculateCost(colS, colT):
    # create m by n matrix
    D=[]
           
    empty_index = colS.index('-') if '-' in colS else len(colS)
    s = colS[:empty_index]
    
    empty_index = colT.index('-') if '-' in colT else len(colT)
    t = colT[:empty_index]
    
    m = len(s)+1
    n = len(t)+1
    
    for i in range(m):
        D.append([])
        for j in range(n):
            D[i].append(0)
    
    for i in range(1, m):
        D[i][0] = i
    for j in range(1, n):
        D[0][j] = n+1
        
    for i in range(1, m):
        for j in range(1, n):
            #calculate min between:
                            
            D[i][j] = min(
                            # deleting
                            D[i-1][j] + 1, 
                            
                            # inserting (only if at the end)
                            # if not last element - give a number > upper bound
                            D[i][j-1] + 1 if (i == m-1) else n+1, 
            
                            # swapping or passing, depending on correctness of 
                            # currently compared items
                            D[i-1][j-1] if (s[i-1]==t[j-1]) else D[i-1][j-1]+1)
    return D[m-1][n-1]
            
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
    columnCost = calculateCost(S[i], T[i])
    #print(a)
    total += columnCost

print(str(int(total)))