import sys

lis_of_numbers = []
counter = 0
upper_limit = 11
bottom_limit = 0
for i in sys.stdin:
    if i == 0:
        break
    if counter % 2 == 0:
        lis_of_numbers.append(int(i.strip()))
    else:
        if i.strip() == 'too high':
            if lis_of_numbers[-1] < upper_limit:
                upper_limit = lis_of_numbers[-1]
        if i.strip() == 'too low':
            if lis_of_numbers[-1] > bottom_limit:
                bottom_limit = lis_of_numbers[-1]
    if i.strip() == "right on":
        if lis_of_numbers[-1] in range(bottom_limit+1,upper_limit):
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        lis_of_numbers = []
        upper_limit = 11
        bottom_limit = 0
    counter += 1
