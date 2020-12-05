#!/usr/bin/python3
#
# https://adventofcode.com/
# 5/12/2020
#
# Day 5
#
# Part 1 was simple
# Part 2 - found the seat quickly but did not submit the ID, thought the challenge was to find the encoded seat which distracted me for 20 minutes.

import re

def find_seat( seat ):
    low = 0
    high = 128
    for l in seat[:7]:
        gap = high - low
        if l == "F":
            high = high - gap / 2
        elif l == "B":
            low = low + gap / 2
    row = low

    low = 0
    high = 8
    for l in seat[7:]:
        gap = high - low
        if l == "L":
            high = high - gap / 2
        elif l == "R":
            low = low + gap / 2
    col = low

    return int(row * 8 + col )

if __name__ == "__main__":
    seat_codes = []
    with open( '5.input.txt' ) as fp:
        for line in fp:
            seat_codes.append( line[:-1] )

    # Part 1
    seats = []
    for seat in seat_codes:
        seats.append( find_seat( seat ) )

    print("Part 1 highest seat ID",max(seats))

    # Part 2
    seats = sorted( seats )

    for i in range(0,len(seats)-1 ):
        if seats[i+1] - seats[i] > 1:
            print( "Part 2 seat ID",int(seats[i] + 1 ) )