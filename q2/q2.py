import time
start_time = time.time()


import sys
import math
file = open('test2.dat') #sys.stdin


items = []
results = []
linenumber = 0
for line in file:
    # if line is not a comment
    if line[:1] != '#':
        linenumber += 1
        if linenumber==1:
            l = int(line.strip())
        elif linenumber==2:
            h = int(line.strip())
        elif linenumber==3:
            s = int(line.strip())
        elif linenumber==4:
            n = int(line.strip())  
        elif line!='\n':
            lineArray = line.strip().split(' ')
            items.append([int(lineArray[1]) + h, int(lineArray[0])])

# sort elements by arrival to ground time
items = sorted(items)

for i in range(0, n):
    time = i[0]
    position = i[1]
    if position > time*s:
        # object is unreachable
        results.append(0)
    else:
        max = 0;
        for k in range(n-1,-1):
            if (k == -1)
                # there is no compatible items to pick up
                results.append(1)
                #distance                 #delta t
            if (math.fabs(items[k][1] - position) < math.fabs(items[k][0]-time) *s)
                results.append(results[k]+1)
            
        


print(time.time() - start_time, "seconds")
