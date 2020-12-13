#!/usr/bin/python3
#
# https://adventofcode.com/
# 13/12/2020
#
# Day 13
#
# Part 1 was straightforward.
# Part 2 is a PITA. Simple exhaustive search algorithm does not scale to the level necessary. Observation is that input data are all prime numbers.
#        That must be sigificant. A look at other peoples solution show it involves some maths I don't have the time to understand. This does raise
#        an interesting dilema. Do I copy someone elses solution in order to get the point even though I don't understand it. I think not. I will 
#        conceed this point due to the lack of time to understand the correct solution. Where I have been inspired by other solutions (once previously
#        in 2020), I have understood the solution and coded my own implementation. Here I just don't understand. Chapeau to the creator.

from math import gcd


if __name__ == "__main__":

    test = True
    filename = '13.input.txt'

    if test:
        filename = '13.input-test.txt'

    earliest = None
    buses = []
    schedule = []

    # parse input file into array 
    with open( filename ) as fp:
        line = fp.readlines()
        # first line is the earliest you can depart
        earliest = int(line[0][:-1])
        for bus in line[1][:-1].split(","):
            if bus != "x":
                buses.append( int( bus ) )
                schedule.append( int(bus) )
            else:
                schedule.append( None )

    earliest_bus = None
    earliest_departure = earliest * 2
    for bus in buses:
        departure = ((int(earliest / bus) + 1) * bus)
        if departure < earliest_departure:
            earliest_departure = departure
            earliest_bus = bus

    print("Part 1:",  (earliest_departure-earliest) * earliest_bus )

    # this is an exhaustive search algorithm that does not scale to the level necessary to solve this part of the problem
    min_bus_number = min(buses)
    t = 0
    while True:
        match = True
        for i in range(len(schedule)):
            if schedule[i]:
                if (t + i) % schedule[i] > 0:
                    match = False
                    break
        if match:
            break
        t += min_bus_number

    print("Part 2:",  t )

