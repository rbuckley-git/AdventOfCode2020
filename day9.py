#!/usr/bin/python3
#
# https://adventofcode.com/
# 9/12/2020
#
# Day 9
#
# Quite a simple problem. One of the quicker ones to solve involving some nice python array slices and manipulation.
#

def is_sum_of_slice_equal_to_target( target, data ):
    for a in data:
        for b in data:
            # rules say sum components need to be unique
            if a != b:
                if a + b == target:
                    return True

    return False

if __name__ == "__main__":

    test = False
    data = []
    preamble = 25
    filename = '9.input.txt'

    if test:
        preamble = 5
        filename = '9.input-test.txt'

    # parse input file into array of ints
    with open( filename ) as fp:
        for line in fp:
            data.append( int( line[:-1] ) )
    
    n = preamble    
    # Starting at preamble, take a slice of preamble size and send it off for checking
    while n < len(data):
        # break at first one that does not match the rules
        if not is_sum_of_slice_equal_to_target( data[n], data[ n-preamble:n ] ):
            break
        n += 1

    print("Part 1:",data[n])

    magic_number = data[n]

    answer = None
    # Test data has four digits as the answer. Question asks for 2 or more. Actual answer turns out ot be 17.
    # Starting with a small range and increasing, extract the range and sum it to test against previous magic answer.
    for i in range(2,len(data)):
        for n in range(0,len(data)-i):
            s = data[n:n+i]
            if magic_number == sum(s):
                answer = max(s)+min(s)
                break
        if answer != None:
            break

    print("Part 2:",answer)