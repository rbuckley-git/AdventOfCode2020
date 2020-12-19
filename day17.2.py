#!/usr/bin/python3
#
# https://adventofcode.com/
# 17/12/2020
#
# Day 17
#
# A few nights off given some work and family commitments. 
# 
# Part 2 - This was easy given part 1. Just add another dimension and apply the same logic. For a change part 2 was easy.

# load data from two dimensions and have the other dimension constant at 0
def load_space( filename ):
    space = {}
    (z,y,w) = (0,0,0)
    with open( filename ) as fp:
        for line in fp:
            line = line[:-1]
            x = 0
            for c in line:
                space[ (x,y,z,w) ] = c
                x += 1
            y += 1

    return space

def get_dimensions( space ):
    ( maxx, maxy, maxz, maxw )  = ( 0, 0, 0, 0)
    ( minx, miny, minz, minw )  = ( 0, 0, 0, 0)

    for s in space.keys():
        if s[0] > maxx:
            maxx = s[0]
        if s[1] > maxy:
            maxy = s[0]
        if s[2] > maxz:
            maxz = s[0]
        if s[3] > maxw:
            maxw = s[0]
        if s[0] < minx:
            minx = s[0]
        if s[1] < miny:
            miny = s[0]
        if s[2] < minz:
            minz = s[0]
        if s[3] < minw:
            minw = s[0]

    return ( minx,miny,minz,minw,maxx,maxy,maxz,maxw )
    
def count_neighbours( space, s ):
    count = 0
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    px = s[0] + x
                    py = s[1] + y
                    pz = s[2] + z 
                    pw = s[3] + w
                    if (px,py,pz,pw) != s:
                        if (px,py,pz,pw) in space:
                            v = space[(px,py,pz,pw)]
                            if v == "#":
                                count += 1

    return count

def print_space( space ):
    (minx,miny,minz,minw,maxx,maxy,maxz,maxw) = get_dimensions( space )
    print("dimensions:",minx,miny,minz,minw,maxx,maxy,maxz,maxw)

    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            print("z =",z,"w =",w)
            for y in range(miny,maxy+1):
                line = ""
                for x in range(minx,maxx+1):
                    if (x,y,z,w) in space:
                        line = line + space[(x,y,z,w)]
                    else:
                        line = line + "."
                print(line)
            print()

# If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.

def cycle( space ):
    changes = {}
    (minx,miny,minz,minw,maxx,maxy,maxz,maxw) = get_dimensions( space )
    for x in range(minx-1,maxx+2):
        for y in range(miny-1,maxy+2):
            for z in range(minz-1,maxz+2):
                for w in range(minw-1,maxw+2):
                    if (x,y,z,w) not in space:
                        space[(x,y,z,w)] = "."

                    c = count_neighbours( space, (x,y,z,w) )

                    v = space[ (x,y,z,w) ]
                    if v == "#":
                        if c not in [2,3]:
                            changes[ (x,y,z,w) ] = "."
                    elif v == ".":
                        if c == 3:
                            changes[ (x,y,z,w) ] = "#"

    space.update( changes )

    return space

def count_cubes( space ):
    count = 0
    for v in space.values():
        if v == "#":
            count += 1
    return count

if __name__ == "__main__":

    test = False
    filename = '17.input.txt'

    if test:
        filename = '17.input-test.txt'

    space = load_space( filename )
    for c in range(6):
        print_space( space )
        space = cycle( space )

    print( "Part 2:", count_cubes( space ) )
