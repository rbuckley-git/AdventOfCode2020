#!/usr/bin/python3
#
# https://adventofcode.com/
# 11/12/2020
#
# Day 11
#
# Both parts straightforward. Took a little longer to complete part 1 as I was distracted making dinner (and hungry). Came back to it after
# some food and nailed it. Part 2 was quick to complete with solution working right first time. Some nice ASCII art animated during execution of part 2.
# The logic behind this puzzle is quite amazing.
#

import copy

# Seat map has following identifiers
#    L = empty
#    # = occupied
#    . = floor

# answer is looking for number of occupied seats so count them
def count_seats( data ):
    count = 0
    for d in data:
        for c in d:
            if c == "#":
                count += 1

    return count

# this counts seats in either of the eight directions around our point
def count_ajacent_seats( data, x, y ):
    width = len(data[0])
    height = len(data)
    count = 0

    pos = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    for p in pos:
        # look at cell in either direction
        (xx,yy) = (x + p[0],y + p[1])

        # whilst we are within the boundary
        if xx >= 0 and yy >= 0 and xx < width and yy < height:
            if data[yy][xx] == "#":
                count += 1

    return count

# this counts occupied seats that can be seen from our point
def count_visible_seats( data, x, y ):
    width = len(data[0])
    height = len(data)
    count = 0

    # 8 directions either way from point
    pos = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

    # for each direction
    for p in pos:
        (xx,yy) = (x,y)         # start at our origin seat
        while True:
            # move in the specified direction
            xx += p[0]
            yy += p[1]

            # whilst we are within the boundary
            if xx >= 0 and yy >= 0 and xx < width and yy < height:
                # if occupied, count the seat and break from loop
                if data[yy][xx] == "#":
                    count += 1
                    break
                # if empty, just break from loop
                if data[yy][xx] == "L":
                    break
            else:
                # outside the boundary, just break from loop
                break

    return count

# useful for debugging
def print_seats( data ):
    for r in data:
        print(r)
    print()

# need to set specific coordinate points to a value, utility method to do this
def set_seat( data, x, y, value):
    s = data[y]
    data[y] = s[:x] + value + s[x+1:]

# solving both parts involves the same logic with some parameters, here the count function is passed in as a parameter along with the tolerence factor
def solve( data, count_fn, tolerence ):
    while True:
        new_data = copy.deepcopy( data ) 
        print_seats( new_data )
        for x in range(len(data[0])):
            for y in range(len(data)):
                count = count_fn( data ,x, y)
                if data[y][x] == "L" and count == 0:
                    set_seat( new_data, x, y, "#")
                elif data[y][x] == "#" and count >= tolerence:
                    set_seat( new_data, x, y, "L")
        if data == new_data:
            break
        data = new_data
    
    return count_seats(data)

if __name__ == "__main__":

    test = False
    filename = '11.input.txt'

    if test:
        filename = '11.input-test.txt'

    data = []

    # parse input file into array of strings
    with open( filename ) as fp:
        for line in fp:
            data.append(  line[:-1] )

    print("Part 1:",  solve( copy.deepcopy( data ),count_ajacent_seats, 4 ) )
    print("Part 2:",  solve( copy.deepcopy( data ),count_visible_seats, 5 ) )

