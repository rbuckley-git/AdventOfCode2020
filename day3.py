#!/usr/bin/python3
#
# https://adventofcode.com/
# 3/12/2020
#
# Day 3
#
# Had to think about this. Wrapping caused me to head scratch as eldest was bothering me.
#

lines = []

def is_tree( x, y ):
    # sort the wrapping out
    width = len( lines[0]) 
    while ( x > width - 1 ):
        x -= width

    if "#" == lines[y][x]:
        return True

    return False

# move according to the vector counting trees as we go until we reach the bottom.
def count_trees( across, down ):
    (x,y) = (0,0)
    trees = 0
    while y < len( lines ):
        if is_tree(x,y):
            trees+=1
        (x,y) = ( x + across, y + down )

    return trees

if __name__ == "__main__":
    with open( '3.input.txt' ) as fp:
        for line in fp:
            lines.append( line[:-1] )

# Right 1, down 1.
# Right 3, down 1.
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

    # probably a nicer way of doing this but it does the job
    a = count_trees( 1, 1 )
    b = count_trees( 3, 1 )
    c = count_trees( 5, 1 )
    d = count_trees( 7, 1 )
    e = count_trees( 1, 2 )

    print("trees",a,b,c,d,e)
    print("product",a*b*c*d*e)