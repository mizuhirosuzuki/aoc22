import numpy as np

# load data
with open('input.txt', 'r') as f:
    snack_array = f.read().split('\n\n')

def str2int(str):
    if str == '':
        return 0
    return int(str)

# part one --------

snack_cons = [np.array(list(map(str2int, snack.split('\n')))).sum() for snack in snack_array]
print(np.max(snack_cons))

# part two --------

snack_cons.sort()
print(np.sum(snack_cons[-3:]))


