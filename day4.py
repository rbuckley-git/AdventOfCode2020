#!/usr/bin/python3
#
# https://adventofcode.com/
# 4/12/2020
#
# Day 4
#
# Nice little parsing and logic challenge. Just bashed the solution out without considering structure or reuse.
#

import re

if __name__ == "__main__":
    passports = []

    # bring all passports onto single lines
    with open( '4.input.txt' ) as fp:
        passport_line = ""
        passport_lines = []
        for line in fp:
            line = line[:-1]
            if len(line)>0:
                passport_line = passport_line + line + " "
            else:
                passport_lines.append( passport_line[:-1] )
                passport_line = ""
        if passport_line:
            passport_lines.append( passport_line[:-1] )

    # parse lines into a fields dict
    for passport_line in passport_lines:
        parts = passport_line.split(" ")
        passport = {}
        for part in parts:
            (tag,value) = part.split(":")
            passport[tag] = value
        passports.append( passport)

    # count passports with all mandatory fields
    valid_passports = 0
    only_valid_passports = []
    for passport in passports:
        valid_fields = 0
        mandatory = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
        for field in mandatory:
            if field in passport:
                valid_fields += 1

        if valid_fields == 7:
            # take a copy of valid passports for use in part 2
            only_valid_passports.append( passport )
            valid_passports += 1

    print("Part 1 - valid passports:",valid_passports)

    # define some reusable rules for field validation
    rules = { 
        "byr": { "type": "number", "length": 4, "gte": 1920, "lte": 2020 },
        "iyr": { "type": "number", "length": 4, "gte": 2010, "lte": 2020 },
        "eyr": { "type": "number", "length": 4, "gte": 2020, "lte": 2030 },
        "hgt": { "type": "height", "cm": { "gte": 150, "lte": 193 }, "in": {"gte": 59, "lte": 76} },
        "hcl": { "type": "rgb"  },
        "ecl": { "type": "one-of", "values": ["amb","blu","brn","gry","grn","hzl","oth" ] },
        "pid": { "type": "number", "length": 9, "gte": 0, "lte": 999999999 }
    }

    # apply the rules above against each field in all valid passports
    valid_passports = 0
    for passport in only_valid_passports:
        valid_fields = 0
        for field in mandatory:
            rule = rules[ field ]
            value = passport[ field ]
            if rule["type"] == "number":
                if len(value) == rule["length"]:
                    v = int( value )
                    if v >= rule["gte"] and v <= rule["lte"]:
                        valid_fields += 1
            elif rule["type"] == "rgb":
                match = re.match("#[0-9a-f]{6}",value)
                if match:
                    valid_fields += 1
            elif rule["type"] == "one-of":
                if value in rule["values"]:
                    valid_fields += 1
            elif rule["type"] == "height":
                match = re.match("(\d+)(cm|in)",value)
                if match:
                    v = int(match.group(1))
                    unit = match.group(2)
                    range = rule[unit]
                    if v >= range["gte"] and v <= range["lte"]:
                        valid_fields += 1
        if valid_fields == 7:
            valid_passports += 1

    print("Part 2 - valid passports:",valid_passports)
