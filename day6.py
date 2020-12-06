#!/usr/bin/python3
#
# https://adventofcode.com/
# 6/12/2020
#
# Day 6
#
# Nice exploration of set intersections. Probably a more Pythonic way of doing several steps but it got the job done (quickly).
#

if __name__ == "__main__":

    total = 0
    with open( '6.input.txt' ) as fp:
        questions = set()
        for line in fp:
            line = line[:-1]
            if len(line)>0:
                # this time, add questions to the existing set, removing duplicates in the process
                for l in line:
                    questions.add( l )
            else:
                total += len(questions)
                questions = set()

        # deal with last group
        total += len(questions)

    print( "Part 1:", total )

    total = 0
    with open( '6.input.txt' ) as fp:
        group = []
        for line in fp:
            line = line[:-1]
            if len(line)>0:
                # this time, create a set for this passenger and add it into an array of questions for the group
                questions = set()
                for l in line:
                    questions.add( l )
                group.append( questions )
            else:
                # establish the intersection of all the sets in the group
                total += len( set.intersection( * map( set, group ) ) )                
                group = []

        # deal with last group
        total += len( set.intersection( * map( set, group ) ) )                

    print( "Part 2:",total )
    