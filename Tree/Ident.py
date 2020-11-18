# Ident -- Parse tree node class for representing identifiers

from Tree import Node
from Print import Printer

class Ident(Node):
    def __init__(self, n):
        self.name = n

    def print(self, n, p=False):
        Printer.printIdent(n, self.name)

    def getName(self):
        return self.name

    def isSymbol(self):
        return True
    
    def eval(self, env):
        return env.lookup(self)

if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
