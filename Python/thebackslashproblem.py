import sys
counter = 0
special_literal = [chr(i) for i in range(33,43)]
special_literal += [chr(i) for i in range(91,94)]
loop_counter = 0
word = ''
for i in sys.stdin:
    if counter % 2 == 0:
        loop_counter = int(i.strip())
    else:
        word = i.strip()
        for j in range(loop_counter):
            exiting_strin = ''
            for k in word:
                if k in special_literal:
                    exiting_strin += '\\' + '{}'.format(k)
                else:
                    exiting_strin += k
            word = exiting_strin
        print(word)
    counter += 1
