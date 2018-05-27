import sys
monster_attacks = sys.stdin.readline().strip()
string = ''
counter = 0
list_for_count = ['RBL','RLB','BLR','BRL','LRB','LBR']
while counter != len(monster_attacks):
    if monster_attacks[counter:counter+3] in list_for_count:
        counter += 3
        string += 'C'
    else:
        string += monster_attacks[counter]
        counter += 1
replace_R = string.replace('R','S')
replace_B = replace_R.replace('B','K')
replace_L = replace_B.replace('L','H')
print(replace_L)
