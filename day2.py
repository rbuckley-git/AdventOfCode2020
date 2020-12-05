#!/usr/bin/python3
#
# https://adventofcode.com/
# 2/12/2020
#
# Day 2
#
# Straightforward challenge.
#

def validate_password1( password, letter, low, high ):
    c = 0
    for ch in password:
        if ch == letter:
            c += 1
    if c >= low and c <= high:
        return True

    return False

def validate_password2( password, letter, low, high ):
    a = password[low - 1]
    b = password[high - 1]

    if a == letter and b == letter:
        return False
    if a == letter or b == letter:
        return True

    return False

if __name__ == '__main__':
    passwords = []
    with open( '2.input.txt' ) as fp:
        valid1 = 0
        valid2 = 0
        for line in fp:
            (a,b) = line[:-1].split(":")
            a = a.strip()
            password = b.strip()
            (a,letter) = a.split(" ")
            (l,h) = a.split("-")
            if validate_password1(password,letter,int(l),int(h)):
                valid1 += 1
            if validate_password2(password,letter,int(l),int(h)):
                valid2 += 1

    print("Valid 1 passwords: ",valid1)
    print("Valid 2 passwords: ",valid2)
            
