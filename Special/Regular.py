# Regular -- Parse tree node strategy for printing regular lists

from Tree import Nil
from Print import Printer
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)

    # evaluate the inside cons node and then use the environment to evaluate the final function (when met with a specific function). 
    # And since eval is likely recursive it populates the environment which is to be used in evaluating the function given
    
    # implements the caller side of a function call
    # apply is callee function of call
    def eval(self, exp, env):
        # if the regular expression is of form:
        # (f x y): regular eval will evaluate all the expressions in turn
        # eval f: suppose it evaluates to Closure c
        # eval x: evaluates to 2 (intLit)
        # eval y: evaluates to 3 (intLit)
        #
        # c.apply(list of evaluated arguments)
        # c.apply( (2 3) )


        # + 2 3
        # (+ x y)
        # EVALUATE PROCEDURE GET CLOSURE OR BUILTIN
        # EVALUATE X, EVALUATE Y
        # CALL APPLY ON THE FUNCTION WE GOT FROM EVALUATING FIRST PART (OPERATOR)

        # to call eval on every list element, that is what we have mapeval for in util.

        if(exp == None):
            print("attempt to call a non-procedure [tail-call]")
            return
        else:
            return exp.getCar.eval(env)