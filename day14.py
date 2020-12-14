#!/usr/bin/python3
#
# https://adventofcode.com/
# 14/12/2020
#
# Day 14
#
# Part 1 was again straightforward with a simple bitwise operation to get the desired values.
# Part 2 was an arse to get right though I am pleased with the solution. Stared at it for far too long though.

def solve_part1( filename ):
    memory = {}

    # parse input file and process inline
    with open( filename ) as fp:
        mask0 = 0
        mask1 = 0
        for line in fp:
            line = line[:-1]
            if line.startswith("mask"):
                mask = line.split(" = ")[1]
                mask0 = int(mask.replace("X","0"),2)
                mask1 = int(mask.replace("X","1"),2)

            elif line.startswith("mem"):
                line = line.replace("mem[","").replace("]","")
                addr = int(line.split(" = ")[0])
                value = int(line.split(" = ")[1])
                memory[addr] = (value | mask0) & mask1

    return sum(memory.values())

def calc_address( addr, mask ):

    # the 1's mask is just a straight bitwise OR. This leaves the maximum value that needs to be fiddled
    # for example XXXX => 1111 with fiddling, this would be 
    #   0000,0001,0010,0011,0100,0101,0110,0111,1000,1001,1010,1011,1100,1101,1110,1111
    # which gives 16 permutations of address
    mask1 = int(mask.replace("X","1"),2)
    addr = addr | mask1

    # create an array of bitmasks for each X character in mask
    p = []
    for i in range(len(mask)):
        if mask[len(mask)-1-i] == "X":
            p.append( 2**i )

    # this was a PITA to get right, need to explode our array into every combination of bitmasks then for each combination
    # a is permutations which is 2^bitmasks e.g. 2 bitmasks would give 4 combinations, 3 would give 8, etc
    addresses = []
    for a in range(2**len(p)):
        sum = 0
        # after lots of trial and error, treat "a" as a bitmask work out the bits that are turned on or off then apply this to the entries in p[]
        for b in range(len(p)):
            c = 2**(b)
            # if turned on, include it in sum
            if a & c == c:
                sum += p[b]
        addresses.append( addr - sum )

    return sorted(addresses)

def solve_part2( filename ):
    memory = {}

    # parse input file into array 
    with open( filename ) as fp:
        mask = None
        for line in fp:
            line = line[:-1]
            if line.startswith("mask"):
                mask = line.split(" = ")[1]

            elif line.startswith("mem"):
                line = line.replace("mem[","").replace("]","")
                addr = int(line.split(" = ")[0])
                value = int(line.split(" = ")[1])
                for a in calc_address( addr, mask ):
                    memory[ a] = value

    return sum(memory.values())

if __name__ == "__main__":

    test = False
    filename = '14.input.txt'

    if test:
        filename = '14.input-test.txt'

    print( "Part 1:", solve_part1( filename ) )
    print( "Part 2:", solve_part2( filename ) )

