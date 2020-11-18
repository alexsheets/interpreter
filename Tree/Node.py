# Node -- Base class for parse tree node objects

import sys
from abc import ABC, abstractmethod

class Node(ABC):
    # The argument of print(int) is the number of characters to indent.
    # Every subclass of Node must implement print(int).

    # The first argument of print(int, bool) is the number of characters
    # to indent.  It is interpreted the same as for print(int).
    # The second argument is only useful for lists (nodes of classes
    # Cons or Nil).  For all other subclasses of Node, the boolean
    # argument is ignored.  Therefore, print(n,p) defaults to print(n)
    # for all classes other than Cons and Nil.
    # For classes Cons and Nil, print(n,TRUE) means that the open
    # parenthesis was printed already by the caller.
    # Only classes Cons and Nil implement print(int, bool).
    # For correctly indenting special forms, you might need to pass
    # additional information to print.  What additional information
    # you pass is up to you.  If you only need one more bit, you can
    # encode that in the sign bit of n. If you need additional parameters,
    # make sure that you define the method print in all the appropriate
    # subclasses of Node as well.
    @abstractmethod
    def print(self, n, p=False):
        pass

    # For parsing Cons nodes, for printing trees, and later for
    # evaluating them, we need some helper functions that test
    # the type of a node and that extract some information.

    # These are implemented in the appropriate subclasses to return true.
    def isBool(self):           # BoolLit
        return False
    def isNumber(self):         # IntLit
        return False
    def isString(self):         # StrLit
        return False
    def isSymbol(self):         # Ident
        return False
    def isNull(self):           # Nil
        return False
    def isPair(self):           # Cons
        return False
    def isProcedure(self):      # BuiltIn, Closure
        return False
    def isEnvironment(self):    # Environment
        return False

    # Report an error in these default methods and implement them
    # in class Cons.  After setCar, a Cons cell needs to be `parsed' again
    # using parseList.
    def getCar(self):
        from Tree import Nil
        self._error("argument of car is not a pair")
        return Nil.getInstance()

    def getCdr(self):
        from Tree import Nil
        self._error("argument of cdr is not a pair")
        return Nil.getInstance()

    def setCar(self, a):
        self._error("argument of set-car! is not a pair")

    def setCdr(self, d):
        self._error("argument of set-cdr! is not a pair")

    def getName(self):
        return ""

    def eval(self, env):
        from Tree import Nil
        self._error("Node.eval not yet implemented")
        return Nil.getInstance()

    def apply(self, env):
        from Tree import Nil
        self._error("Node.eval not yet implemented")
        return Nil.getInstance()

    def _error(self, msg):
        sys.stderr.write("Error: " + msg + "\n")
        sys.stderr.flush()
