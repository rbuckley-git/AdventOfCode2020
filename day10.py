#!/usr/bin/python3
#
# https://adventofcode.com/
# 10/12/2020
#
# Day 10
#
# Part 1 was easy.
# Part 2 was hard. Wrote a recursive solution but quit that when the computer started to lift off. Quickly realised it was not solvable that way.
# Knew the trick with with the runs of sequences making up the permuations an that the skew of the data showd only gaps of 1 or 3. This bounds the problem a little.
# After staring at the screen for longer than was healthy, took "inspiration" from other solutions and taking the hint, wrote my own version. Solution is a mahoosive number.
#

def find_adapter( input, data ):
    rng = list(range(input + 1, input+4))
    for r in rng:
        for i in range( 0, len(data) ):
            if data[i] == r:
                return data[i]
    return None

def solve_part1( data ):
    # include our device into the list
    data.append( max(data) + 3 )
    data = sorted(data)

    input = 0
    differences = {}
    while len(data)>0:
        value = find_adapter( input, data )
        data.remove( value )
        diff = value - input
        input = value
        if diff not in differences:
            differences[diff] = 1
        else:
            differences[diff] += 1

    return differences[1] * differences[3]

def solve_part2( data ):

    # include the outlet and our device into the list as these provide permutations to consider
    data.append( 0 )
    data.append( max(data) + 3 )
    data = sorted(data)

    # we know from part 1 that we only have gaps of 1 or 3. It is the gaps of 1 that are significant in permutations.
    # the skew of the data shows runs of 1,2,3,4 with gap of 1
    # a run of 2 has 2 combinations
    # a run of 3 has 4 combinations
    # a run of 4 has 7 combinations 
    n = 0
    combinations = 1
    for i in range(0,len(data)-1):
        # are we a run of 1, if so, count the number of 1s we have
        if data[i+1] - data[i] == 1:
            n += 1
        else:
            if n == 2:
                combinations *= 2 
            elif n == 3:
                combinations *= 4
            elif n == 4:
                combinations *= 7
            n = 0

    return combinations

if __name__ == "__main__":

    test = False
    filename = '10.input.txt'

    if test:
        filename = '10.input-test2.txt'

    data = []

    # parse input file into array of ints
    with open( filename ) as fp:
        for line in fp:
            data.append( int( line[:-1] ) )
    
    print("Part 1:",solve_part1( data.copy() ) )
    print("Part 2:",solve_part2( data.copy() ) )
