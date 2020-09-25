


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





















if __name__ == "__permutation_counter__":
    from permutator import permuter
    permutations = permuter(3)
    for permutation in permutations:
        print(permutation)
        print(permutation_counter(permutation))
        print("")
