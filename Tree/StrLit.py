# StLit -- Parse tree node class for representing string literals

import sys
from Tree import Node
from Print import Printer

class StrLit(Node):
    def __init__(self, s):
        self.strVal = s

    def print(self, n, p=False):
        # if bool is true, then it would contain code that was there before
        # print n spaces, print strVal without double quotes
        # if n>=0 print newline char
        # if executing write, then call printStrLit
        Printer.printStrLit(n, self.strVal)

    def isString(self):
        return True
    
    def eval(self, env):
        return self

if __name__ == "__main__":
    id = StrLit("foo")
    id.print(0)
