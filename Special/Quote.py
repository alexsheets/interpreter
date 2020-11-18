# Quote -- Parse tree node strategy for printing the special form quote

from Tree import Nil
from Print import Printer
from Special import Special

class Quote(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printQuote(t, n, p)
    
    def eval(self, exp, env):
        # add error checks etc.
        # example: don't call getCar if getCdr empty...
        return exp.getCdr().getCar()
