from itertools import permutations as permute

def permutations(s):
    bank = []
    perm = permute(s)
    for i in perm:
        bank.append(''.join(i))
    return set(bank)