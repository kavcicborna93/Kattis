import sys
number = int(sys.stdin.readline().strip())
steps = 0
for i in range(2,int(number**0.5)+1):
    while number % i == 0:
        number /= i
        steps +=1
if number != 1:
    steps += 1
print(steps)
