# Lambda -- Parse tree node strategy for printing the special form lambda

from Tree import Closure
from Print import Printer
from Special import Special

class Lambda(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printLambda(t, n, p)
    
    def eval(self, exp, env):
        return Closure(exp, env)
