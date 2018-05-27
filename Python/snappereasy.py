import sys, os

numberOfCases = int(sys.stdin.readline())

for i in range(numberOfCases):
    data = sys.stdin.readline().split()
    snapperdevices, ktimes = map(int, data)
    print ("Case #%d:" % (i+1))
    for j in range(snapperdevices):
        if ktimes & (2**j) == 0:
            print ("OFF")
            break
    else:
        print ("ON")

