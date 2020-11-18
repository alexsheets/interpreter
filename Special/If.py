# If -- Parse tree node strategy for printing the special form if

from Tree import BoolLit
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printIf(t, n, p)

    def eval(self, exp, env):
        # what if no else part for if? condition
        # look at language definition for if; if there is no then, return is unspecified
        # if there is an if then used inside the begin but not as the last expression, and we know the condition 
        # evaluate what then does and otherwise keep going inside begin
        # return nil.getinstance when unspecified

        # for define, it can be unspecified as well, you can return nil.getinstance
        
        pass
