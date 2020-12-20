#!/usr/bin/python3
#
# https://adventofcode.com/
# 20/12/2020
#
# Day 18
#
# Both parts were tough. Trick seems to be the handling of the parenthesis and evaluating that, using replace to swap out the equation for the answer.
# Part 1 was left to right, part 2 was addition over parenthesis.

import re

# Part 1 calculations. This worked with just regular expressions.
def calculate1( line ):

    # Sort out the parenthesis. Keep recursing for each parenthesis block found. Swap answer in place of the equation.
    parentheses = True
    while parentheses:
        match = re.match(".*\(([^\)]*)\)",line)
        if match:
            a = calculate1( match.group(1) ) 
            line = line.replace(  "(" + match.group(1) + ")", str(a) )
        else:
            parentheses = False
            match = re.match("^(\d+)\s\*\s(\d+)$",line)
            if match:
                return int(match.group(1)) * int(match.group(2))

            match = re.match("^(\d+)\s\+\s(\d+)$",line)
            if match:
                return int(match.group(1)) + int(match.group(2))
            
    # Sit in a loop evaluating from left to right until we have just a single number remaining    
    while True:
        match = re.match("^(\d+)$",line)
        if match:
            return int(match.group(1))

        match = re.match("^(\d+)\s\*\s(\d+)",line)
        if match:
            a = int(match.group(1)) * int(match.group(2))
            line = line.replace( match.group(1) + " * " + match.group(2), str(a),1 )
        else:
            match = re.match("^(\d+)\s\+\s(\d+)",line)
            if match:
                a = int(match.group(1)) + int(match.group(2))
                line = line.replace( match.group(1) + " + " + match.group(2), str(a),1 )

    return None

# Part 2 calculations
def calculate2( line ):

    # Identical parenthesis handling to part 1
    parentheses = True
    while parentheses:
        match = re.match(".*\(([^\)]*)\)",line)
        if match:
            a = calculate2( match.group(1) ) 
            line = line.replace(  "(" + match.group(1) + ")", str(a), 1 )
        else:
            parentheses = False
            match = re.match("^(\d+)\s\*\s(\d+)$",line)
            if match:
                return int(match.group(1)) * int(match.group(2))

            match = re.match("^(\d+)\s\+\s(\d+)$",line)
            if match:
                return int(match.group(1)) + int(match.group(2))

    # This time it is not left to right but addition over multiplication.
    # Split by multiplication symbol to get the parts that need to be added together.
    for s in line.split(" * "):
        a = 0
        for t in s.split(" + "):
            a += int(t)
        line = line.replace( s, str(a), 1 )

    # Then resolve the multiplications
    a = 1
    for s in line.split(" * "):
        a *= int(s)

    return a


if __name__ == "__main__":

    test = False
    filename = '18.input.txt'

    if test:
        filename = '18.input-test.txt'

    part1_answer = 0
    part2_answer = 0
    with open( filename ) as fp:
        for line in fp:
            line = line[:-1]
            part1_answer += calculate1( line )
            part2_answer += calculate2( line )

    print( "Part 1:", part1_answer )
    print( "Part 2:", part2_answer )
