#!/usr/bin/python3
#
# https://adventofcode.com/
# 12/12/2020
#
# Day 12
#
# Nice little problem this. Only niggle was rotation around the vessel in part 2.
#

def move_forwards(x,y,dir,v):
    if dir == "E":
        x += v
    elif dir == "N":
        y += v
    elif dir == "S":
        y -= v
    elif dir == "W":
        x -= v

    return (x,y)

# simplified by all rotations being multiples of 90 degs.
def rotate( dir, v):
    r = int(v/90)
    directions = [ 'E','S','W','N']
    p = directions.index(dir)

    return directions[(p + r) % len(directions)]

# part 1 problem
def navigate_ship(x,y,dir,data):
    for ins in data:
        if ins["op"] == "F":
            (x,y) = move_forwards(x,y,dir,ins["v"])
        elif ins["op"] == "N":
            y += ins["v"]
        elif ins["op"] == "S":
            y -= ins["v"]
        elif ins["op"] == "W":
            x -= ins["v"]
        elif ins["op"] == "E":
            x += ins["v"]
        elif ins["op"] == "R":
            dir = rotate(dir, ins["v"])    
        elif ins["op"] == "L":
            dir = rotate(dir, -1 * ins["v"])    

    return (x,y)

# in this part, we move v times with the vector from x,y to wx,wy. For each move, the waypoint wx,wy also moves.
def move_towards_waypoint(x,y,wx,wy,v):
    dx = wx - x
    dy = wy - y

    x += ( dx * v )
    y += ( dy * v )
    wx += ( dx * v )
    wy += ( dy * v )

    # both ship and waypoint will have moved
    return (x,y,wx,wy)

# the trick here was to make the ship the origin for the rotation then put the ship back in at the end
def rotate_waypoint(x, y, wx,wy,v):
    # make ship the origin
    wx -= x
    wy -= y

    # deal with both positive and negative rotations
    r = int(v/90) % 4

    # actually used a peice of paper for these matrix calculations. Most likely a neater pythonic way of doing it.
    if r == 1:
        wx2 = wx *  0 + wy * 1
        wy2 = wx * -1 + wy * 0
    elif r == 2:
        wx2 = wx * -1 + wy * 0
        wy2 = wx *  0 + wy * -1
    elif r == 3:
        wx2 = wx *  0 + wy * -1
        wy2 = wx *  1 + wy *  0

    # offset waypoint by ship again
    wx2 += x
    wy2 += y

    return (wx2,wy2)

# part 2 problem
def navigate_with_waypoint(x,y,wx,wy):
    for ins in data:
        if ins["op"] == "F":
            (x,y,wx,wy) = move_towards_waypoint(x,y,wx,wy,ins["v"])
        elif ins["op"] == "N":
            wy += ins["v"]
        elif ins["op"] == "S":
            wy -= ins["v"]
        elif ins["op"] == "W":
            wx -= ins["v"]
        elif ins["op"] == "E":
            wx += ins["v"]
        elif ins["op"] == "R":
            (wx,wy) = rotate_waypoint(x, y, wx, wy, ins["v"])    
        elif ins["op"] == "L":
            (wx,wy) = rotate_waypoint(x, y, wx, wy, -1 * ins["v"])    

    return (x,y)

if __name__ == "__main__":

    test = False
    filename = '12.input.txt'

    if test:
        filename = '12.input-test.txt'

    data = []

    # parse input file into array of operations with integer arguments
    with open( filename ) as fp:
        for line in fp:
            instruction = {}
            instruction["op"] = line[0:1]
            instruction["v"] = int(line[1:-1])
            data.append(  instruction )

    (x,y) = navigate_ship(0, 0, "E", data)
    print("Part 1:",  abs(x) + abs(y) )

    (x,y) = navigate_with_waypoint(0, 0, 10, 1)
    print("Part 2:",  abs(x) + abs(y) )

