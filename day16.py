#!/usr/bin/python3
#
# https://adventofcode.com/
# 16/12/2020
#
# Day 16
#
# Part 1 easy.
# Part 2 went down a rabbit hole that worked for the test data but kept on returning random orders for the actual input data. That was looking at the problem
# ticket-wise building up a list of fields that were applicable. Tried a load of things before going back to the test data and staring hard again. Tried
# the problem field-wise and it started taking shape with one rule that is only completely satisfied by one field. Then it is a case of removing that field and
# hoping another one appears with just one entry. It does. Probably a more pythonic way of dealing with these arrays and doing array subtraction. Too late for that.

def validate_ticket( ticket, fields ):
    error = 0
    for x in ticket:
        found = False
        for v in fields.values():
            if x in v:
                found = True
                break
        if not found:
            error += x

    return error

def find_valid_fields( id, fields, exclude ):
    found = []
    for f,v in fields.items():
        if f not in exclude:
            if id in v:
                found.append( f )

    return found

def solve_part1( nearby_tickets, fields ):

    error_rate = 0
    for nearby in nearby_tickets:
        error_rate += validate_ticket( nearby, fields )

    return error_rate

def solve_part2( ticket, nearby_tickets, fields ):

    # we need to remove any tickets that did not pass validation so build a new array with just the good ones
    valid_tickets = []
    for nearby in nearby_tickets:        
        if validate_ticket( nearby, fields ) == 0:
            valid_tickets.append( nearby )

    # constants for later use
    number_fields = len(valid_tickets[0])
    number_tickets = len(valid_tickets)

    # solving the problem field-wise, based on the test data of seat, class, row, one of this only has a valid single column
    field_hash = {}
    for field,ids in fields.items():
        # container for columns that 
        r = []
        # look at each column in the ticket
        for c in range(number_fields):
            count = 0
            # and each ticket element matching the ids for the field
            for v in valid_tickets:
                if v[c] in ids:
                    count += 1
            # where all tickets satisfy this field, add the column to our list
            if count == number_tickets:
                r.append( c )
        # stash the matching columns against field name
        field_hash[field] = r

    # place holder for our fields in order, creating of right size so entries can just be set
    found_fields = ["unknown" for x in range(number_fields)]

    # as we find entries, add them to an ignore list so they can be excluded later
    ignore_list = []
    for i in range(number_fields):
        for k,v in field_hash.items():
            # build list of column ids that are not on the ignore list
            w = []
            for id in v:
                if id not in ignore_list:
                    w.append(id)
                    
            # is there just a single entry for this field, bingo, set it up and add it to be ignored
            if len(w) == 1:
                found_fields[w[0]] = k
                ignore_list.append(w[0])

    # trival iteration with filter to get the answer
    answer = 1
    for i in range(number_fields):
        if found_fields[i].startswith("departure"):
            print(i,found_fields[i],ticket[i])
            answer *= ticket[i]

    return answer


if __name__ == "__main__":

    test = False
    filename = '16.input.txt'

    if test:
        filename = '16.input-test.txt'

    ticket = []
    nearby_tickets = []
    fields = {}

    with open( filename ) as fp:
        your = False
        near = False
        for line in fp:
            line = line[:-1]
            if line == "your ticket:":
                your = True
            elif line == "nearby tickets:":
                near = True
            elif line == "":
                None
            else:
                if not your and not near:
                    (key,values) = line.split(": ")
                    valid_values = []
                    for v in values.split(" or "):
                        (l,h) = v.split("-")
                        for x in range(int(l),int(h)+1):
                            valid_values.append( x )

                    fields[key] = valid_values
                elif your and not near:
                    for v in line.split(","):
                        ticket.append( int(v) )
                elif near:
                    f = []
                    for v in line.split(","):
                        f.append( int(v) )
                    nearby_tickets.append( f )
    #print(ticket)
    #print(nearby_tickets)
    #print(fields)

    print( "Part 1:", solve_part1( nearby_tickets, fields ) )
    print( "Part 2:", solve_part2( ticket, nearby_tickets, fields ) )

