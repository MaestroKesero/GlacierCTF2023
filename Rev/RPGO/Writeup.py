gdb script that prints the current maze state after every input:

import gdb

MAZE_BASE = 0x553820

def dump_maze():
    for y in range(0, 10):
        for x in range(0, 10):
            offset = y * 160 + x * 16
            length = int(gdb.parse_and_eval(f"*(unsigned long long*) {MAZE_BASE + offset + 8}"))
            ptr = int(gdb.parse_and_eval(f"*(unsigned long long*) {MAZE_BASE + offset}"))

            assert length == 1
            char = int(gdb.parse_and_eval(f"*(char*) {ptr}"))
            print(chr(char), end="")
        print()

class ReadBP(gdb.Breakpoint):
    def stop(self):
        dump_maze()
    
        return False

ReadBP("*0x49236C")
gdb.execute("handle SIGTRAP nostop noprint noignore nopass") # wtf golang
gdb.execute("run")


Run as gdb -x script.py ./rpgo then just play as normal
