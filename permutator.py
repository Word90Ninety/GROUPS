
from itertools import permutations
from group import Group
from cayley_tabler import cayley_tabler


#TO-DO: fix permutation composer? surely it can't be right
#or whatever is making a3 not be commutative


def xor(first, second):
    if first == second:
        return(1)
    else:
        return(2)

def permuter(size):
    base = ""
    for i in range(size):
        base = base + str(i+1)
    perms = [''.join(p) for p in permutations(base)]
    return(perms)

def permutation_counter(string):
    size = len(string)
    base = ""
    for i in range(size):
        base = base + str(i+1)
    scrambled = [number for number in string]

    swaps = 0
    for position in range(size):
        ideal = position + 1
        actual = scrambled[position]
        #ie. the proper value for the position should be the place number

        if int(actual) != ideal:
            #if it isn't:
            for location in range(size):
                if int(scrambled[location]) == int(ideal):
                    break
            #find where the proper value actually is
            scrambled[location] = str(actual)
            #put the actual value there
            scrambled[position] = str(int(ideal))
            #put the proper value where it should be
            swaps += 1
    return(swaps)

def even_permuter(size):
    allPerms = permuter(size)

    base = ""
    for i in range(size):
        base = base + str(i+1)

    evenPerms = []
    for perm in allPerms:
        if permutation_counter(perm)%2 == 0:
            evenPerms.append(perm)
    return(evenPerms)

def permutation_composer(perm1, perm2):
    #123    123
    #132    231

    #123    132
    #132    213

    #123
    #213
    
    newPerm = []
    for position in range(len(perm1)):
        slot = perm1[position]
        element = perm2[int(slot)-1] 
        newPerm.append(element)
    return("".join(newPerm))

























"""
if __name__ == "__ain__":
    pers = permuter(3)
    for p in pers:
        for pe in pers:
            print(p)
            print(pe)
            print(permutation_composer(p, pe))
            print("")

    print(permuter(3))
    print(even_permuter(3))
    print("")
    simplify = False
    alls = cayley_tabler(Group(permuter(3), permutation_composer), simplify)
    for line in alls:
        print(line)
    print("")
    evens = cayley_tabler(Group(even_permuter(3), permutation_composer), simplify)
    for line in evens:
        print(line)
elif __name__ == "__permutator__":
    evens = cayley_tabler(Group(even_permuter(4), permutation_composer), True)
    for line in evens:
        print(line)
"""















    
    
