import sys
import math
file = sys.stdin

#convert input array as [time@ground, position]
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
            #store items as [time@ground, position]
            items.append([int(lineArray[1]) + h, int(lineArray[0])])

# sort elements by arrival to ground time
items = sorted(items)

# for every element in the list
for i in range(0, n):
    t = items[i][0] #time
    p = items[i][1] #position
    # if object is unreachable, append 0
    if p > t*s:
        results.append(0)
    # first item
    #elif i == 0:
        #results.append(1)
    else:
        # find the most recent compatible item
        for k in range(i-1, -2, -1):
            # if you've iterated through everything, and nothing is compatible
            if (k == -1):
                results.append(1) # append just the one item - 1

            # if compatible interval is found, add the value of it + 1 to results
                      #delta p                 # delta t      *  s
            elif math.fabs(items[k][1] - p) <= (math.fabs(items[k][0]-t) * s):
                results.append(results[k]+1)
                break;
            
        

## timing stuff
#print(time.time() - start_time, "seconds")

## Testing to view all results
#print(results)

print(str(max(results)))

## timing stuff
#print(time.time() - start_time, "seconds")