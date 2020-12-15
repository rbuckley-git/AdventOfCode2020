#!/usr/bin/python3
#
# https://adventofcode.com/
# 15/12/2020
#
# Day 15
#
# Nice easy one. Part 1 could be done without memory pruning. Part 2 was just brute forced in about 20s on my MacBook.

def solve( nth ):
    memory = {}
    value = None
    
    for i in range(1,nth+1):
        if i < len(input)+1:
            # pull initial entries from the input data
            value = input[i-1]
        else:
            # implement the rules
            if value in memory and len(memory[value]) == 1:
                value = 0    
            else:
                a = memory[value]
                # trim the memory to make sure we just have value entry
                memory[value] = [a[-1]]
                # calculate the next value
                value = a[-1] - a[-2]
        
        # debug progress
        if i % 1000000 == 0:
            print(i,"speak",value,len(memory))

        if value in memory:
            turns = memory[value]
            turns.append(i)
            memory[value] = turns
        else:
            memory[value] = [i]

    return value

if __name__ == "__main__":

    test = False
    input = [15,12,0,14,3,1]

    if test:
        input = [0,3,6]

    print( "Part 2:", solve(2020) )
    print( "Part 2:", solve(30000000) )

