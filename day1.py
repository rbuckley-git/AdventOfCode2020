#!/usr/bin/python3
#
# https://adventofcode.com/
# 1/12/2020
#
# Day 1
#
# Straightforward challenge.
#

if __name__ == '__main__':
    items = []
    with open( '1.input.txt' ) as fp:
        for line in fp:
            items.append( int( line[:-1] ) )

    found = False
    for a in items:
        for b in items:
            if a + b == 2020:
                print( "Part 1:", a * b )
                found = True
                break
        if found:
            break

    found = False
    for a in items:
        for b in items:
            for c in items:
                if a + b + c == 2020:
                    print( "Part 2:", a * b * c )
                    found = True
                    break
            if found:
                break
        if found:
            break
