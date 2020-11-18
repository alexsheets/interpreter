# IntLit -- Parse tree node class for representing integer literals

from Tree import Node
from Print import Printer

class IntLit(Node):
    def __init__(self, i):
        self.intVal = i

    def print(self, n, p=False):
        Printer.printIntLit(n, self.intVal)

    def isNumber(self):
        return True
    
    def eval(self, env):
        return self

if __name__ == "__main__":
    id = IntLit(42)
    id.print(0)
