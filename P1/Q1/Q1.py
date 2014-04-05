import sys
import math
file = sys.stdin


# determins if i and j can communitate with each other            
def reachable(transmitters, i, j):
    a = transmitters[i]
    b = transmitters[j]
    distance = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return (distance <= a[2]+b[2])

#main
transmitters = [] # list of all transmitters [x, y, r]
# convert input into an array containing [x, y, r]
linenumber = 0
for line in file:
    # if line is not a comment
    if line[:1] != '#':
        linenumber += 1
        if linenumber==1:
            n = int(line.strip())
            neighbours = [[] for i in range(n)] # 2d array of neighbours
        elif line!='\n':
            lineArray = line.strip().split(' ')
            transmitters.append([float(x) for x in lineArray])

available = []
for i in range(1, n):
    available.append(i)

# results[i] storing H(i, cost)
results = []
for i in range(0, n):
    results.append(0)

#queue of nodes to exmaine: [node, cost]
queue = []
queue.append([0, 0])

while queue != []:
    v = queue.pop(0)
    # add v into results
    results[v[0]] = v[1]
    
    # find neighbours of v and add them into queu with cost v[1]+1
    for a_index in range(len(available)-1, -1, -1):
        if reachable(transmitters, v[0], available[a_index]):
            queue.append([available[a_index], v[1]+1])
            available.pop(a_index)
    

# print results:   
for result in results:
    print(result)

