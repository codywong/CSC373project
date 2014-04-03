import sys
import math
file = open('test3.dat') #sys.stdin


            
def reachable(transmitters, i, current):
    a = transmitters[i]
    b = transmitters[current]
    distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return (distance <= a[2]+b[2])

#main
transmitters = [] # list of all transmitters [x, y, r]

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
            current = len(transmitters)-1
            for i in range(0, current):
                if reachable(transmitters, i, current):
                    neighbours[i].append(current)
                    neighbours[current].append(i)


#queue storing [cost, transmitter]
queue = [[0, 0]]
for i in range(1, len(transmitters)):
    queue.append([float("inf"), i])

# results[i] = H(1, i)    
results = [None]*n
while queue != []:
    u = min(queue)
    queue.remove(u)
    tNumber = u[1]
    tCost = u[0]
    results[tNumber] = tCost
    for neighbour in neighbours[tNumber]:
        for v in queue:
            if v[1] == neighbour:
                v[0] = min( 1+tCost , v[0] )

    
print(results)
                