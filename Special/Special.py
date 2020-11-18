# Special -- Parse tree node strategy for printing special forms

import sys
from abc import ABC, abstractmethod
from Tree import Nil
from Tree import Cons

# There are several different approaches for how to implement the Special
# hierarchy.  We'll discuss some of them in class.  The easiest solution
# is to not add any fields and to use empty constructors.

class Special(ABC):
    util = None

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    @abstractmethod
    def print(self, t, n, p):
        pass

    # added by us
    @abstractmethod
    def eval(self, exp, env):
        pass

    def _error(self, msg):
        sys.stderr.write("Error: " + msg + "\n")
        sys.stderr.flush()
