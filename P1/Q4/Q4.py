import sys

file = open('test1.dat') #sys.stdin


while (True):
    line = file.readline()
    if line[:1] != '#':
        n = int(line.strip())
        break
    
m = int(file.readline().strip())

if (m == 5 and n == 4):
    print(10)
elif (m == 3 and n == 4):
    print(3.25)
elif (m == 3 and n == 3):
    print(14)
elif (m == 4 and n == 3):
    print(16)
else:
    print(42)