#!/usr/bin/python3
#
# https://adventofcode.com/
# 4/12/2020
#
# Day 4
#
# Challenge was just knowing the direction in which to naviate the map created during the file parse.
# First part involved building a set and counting the entries.
# Second part was (as usual), a little more involved with some logic to include the bag itself plus the contents of anyting contained.
# Test input file very useful in checking the calculations.
#

rules = {}
part1 = set() 

# find bags and add to a set, the answer is the unique entries in the set
def find_bag( colour ):
    global part1

    for rule in rules.keys():
        bags = rules[rule]
        for bag in bags:
            if bag["desc"] == colour:
                part1.add( rule )
                find_bag( rule )

# recurse through counting bags and containers
def count_bags( colour ):
    count = 0

    if colour in rules:
        for contain in rules[colour]:
            count += contain["quan"] * (1 + count_bags( contain["desc"]  ))

    return count


if __name__ == "__main__":

    # parse input file into dict of array of dicts
    with open( '7.input.txt' ) as fp:
        for line in fp:
            line = line[:-1]
            line = line.replace(" bags.","").replace(" bags","")
            line = line.replace(" bag.","").replace(" bag","")  
            ( colour, l ) = line.split(" contain ")

            bags = []
            for item in l.split(", "):
                ( quantity, description ) = item.split(" ",1)

                if quantity != "no":
                    bag = {}
                    bag["quan"] = int(quantity)
                    bag["desc"] = description
                    bags.append( bag )

            rules[colour] = bags
    
    find_bag( "shiny gold" )
    print("Part 1:",len(part1))

    print("Part 2:",count_bags("shiny gold"))

