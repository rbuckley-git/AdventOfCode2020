#!/usr/bin/python3
#
# https://adventofcode.com/
# 8/12/2020
#
# Based on experience from last year, started this computer as a class.
#
import copy

class computer:
    def __init__(self, filename ):
        self.prog = self.load_program( filename )
        self.reset()

    def reset( self ):
        self.pc = 0
        self.accumulator = 0
        self.aborted = False

    # parse lines into a structure like this {'code': 'acc', 'arg': 9}
    def load_program( self, filename ):
        with open( filename ) as fp:
            prog = []
            for line in fp:
                op = {}
                line = line[:-1]
                (opcode,arg) = line.split(" ")
                arg = arg.replace("+","")
                op["code"] = opcode
                op["arg"] = int(arg)
                prog.append(op)
            return prog

    def set_aborted( self ):
        self.aborted = True

    def is_aborted( self ):
        return self.aborted

    def get_program( self ):
        return self.prog

    def set_program( self, prog ):
        self.prog = prog

    def execute( self ):
        # set to look for instructions being called a second time
        execution_set = set()

        # whilst we have program to execute
        while self.pc < len( self.prog ):
            # check for pre-execution of this pc value
            if self.pc in execution_set:
                self.set_aborted()
                break

            op = self.prog[ self.pc ]
            execution_set.add( self.pc )

            if op["code"] == "acc":
                self.accumulator += op["arg"]
                self.pc += 1
            elif op["code"] == "nop":
                self.pc += 1
            elif op["code"] == "jmp":
                self.pc += op["arg"]

        return self.accumulator

if __name__ == "__main__":
    boot = computer( "8.input.txt" )
    acc = boot.execute()
    print("Part 1", acc )

    # take a copy of the program code as we want to try stuff and keep restoring original code
    prog_copy = copy.deepcopy( boot.get_program() )
    
    # make a modification to the program, try it, if it aborts, restore copy and move to next modification
    i = 0
    while True:
        prog = copy.deepcopy( prog_copy )

        for j in range( i, len( prog ) ):
            op = prog[ j ]
            i += 1
            if op["code"] == "jmp":
                op["code"] = "nop"
                prog[ j ] = op
                break
            
        boot.set_program( prog )
        boot.reset()
        acc = boot.execute()

        if not boot.is_aborted():
            break
            
    print("Part 2", acc )
