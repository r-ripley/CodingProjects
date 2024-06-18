from itertools import permutations as permute

def permutations(s):
    # create a new list and add each permutation to it
    bank = []
    perm = permute(s)
    for i in perm:
        bank.append(''.join(i))
    return set(bank)