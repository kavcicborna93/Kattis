from itertools import product
import sys

number_of_loops = int(sys.stdin.readline().strip())
for i in range(number_of_loops):
    number = int(sys.stdin.readline().strip())
    for op1,op2,op3 in product(['+','-','//','*'],repeat=3):
        if eval('4 {0} 4 {1} 4 {2} 4'.format(op1,op2,op3)) == number:
            string = '4 {0} 4 {1} 4 {2} 4 = {3}'.format(op1,op2,op3,number)
            new_str = string.replace('//','/')
            print(new_str)
            break
    else:
        print('no solution')
    
