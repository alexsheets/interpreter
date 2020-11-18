# BuiltIn -- the data structure for built-in functions

# Class BuiltIn is used for representing the value of built-in functions
# such as +.  Populate the initial environment with
# (name, BuiltIn(name)) pairs.

# The object-oriented style for implementing built-in functions would be
# to include the Python methods for implementing a Scheme built-in in the
# BuiltIn object.  This could be done by writing one subclass of class
# BuiltIn for each built-in function and implementing the method apply
# appropriately.  This requires a large number of classes, though.
# Another alternative is to program BuiltIn.apply() in a functional
# style by writing a large if-then-else chain that tests the name of
# the function symbol.

import sys
from Parse import *
from Tree import Node
from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import TreeBuilder
#from Tree import Unspecific

class BuiltIn(Node):
    # needed for implementing load function to load something into the environment
    # also need to implement a loop like the one at bottom of scheme4101
    # except dont print anything
    # for builtin function load you need access to environment 
    # and for implementing builtin function interaction env. should return a pointer to this environment
    # so we need to be able to find it inside of this class, builtin.
    env = None
    util = None

    @classmethod
    def setEnv(cls, e):
        cls.env = e

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, s):
        self.symbol = s                 # the Ident for the built-in function

    def getSymbol(self):
        return self.symbol

    def isProcedure(self):
        return True
    
    def eval(self, env):
        from Tree import Nil
        self._error("No eval necessary for BuiltIn.")
        return Nil.getInstance()

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Built-In Procedure ")
        if self.symbol != None:
            self.symbol.print(-abs(n) - 1)
        sys.stdout.write('}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    def apply(self, args):

        # for implementing display, set boolean then print and then set it back towhere it was before
        # as a hack for strLit

        # args[0] = name of the func
        # rest of args are the actual arguments

        # grab name of operation and number of arguments passed
        name = str(args[0])
        count = 0
        for arg in args:
            count += 1

        # TODO: READ, WRITE, INTERACTION ENV?

        # MISC/IO
        if name == 'procedure?':
            if callable(args[0]):
                return BoolLit(True)
            else:
                return BoolLit(False)
        elif name == 'symbol?':
            if isinstance(args[1], str):
                return BoolLit(True)
            else:
                return BoolLit(False)
        elif name == 'display':
            val = args[1]
            if isinstance(val, str) and val.startswith('"'):
                val = StrLit(val)
                val = eval(val)
            print(str(val), end="")
        elif name == 'newline':
            print()
            sys.stdout.flush()
        elif name == "load":
            if not arg1.isString():
                self._error("wrong type of argument")
                return Nil.getInstance()
            filename = arg1.getStrVal()
            try:
                scanner = Scanner(open(filename))
                builder = TreeBuilder()
                parser = Parser(scanner, builder)

                root = parser.parseExp()
                while root != None:
                    root.eval(BuiltIn.env)
                    root = parser.parseExp()
            except IOError:
                self._error("could not find file " + filename)
            return Nil.getInstance()  # or Unspecific.getInstance()
        
        # LIST STUFF
        if name == 'car':
            _list = args[1]
            return _list.getCar()
        elif name == 'cdr':
            _list = args[1]
            return _list.getCdr()
        elif name == 'set-car!':
            _list = args[1]
            _list.setCar(args[2])
            return Nil().getInstance()
        elif name == 'set-cdr!':
            _list = args[1]
            _list.setCdr(args[2])
            return Nil().getInstance()
        elif name == 'cons':
            return Cons(args[1], args[2])
        elif name == 'null?':
            return BoolLit(args[1] is None)
        elif name == 'pair?':
            if isinstance(arguments[1], Cons):
                return BoolLit(True)
            else:
                return BoolLit(False)
        elif name == 'eq?':
            first = args[1]
            second = args[2]
            if (first == second):
                return BoolLit(True)
            else:
                return BoolLit(False)

        # NUMBERS/BINARY OPERATORS
        if name == 'number?':
            if isinstance(args[1], int):
                return BoolLit(True)
            else:
                return BoolLit(False)
        elif name == 'b+':
            total = 0
            # ignore first arg[0], as it is 'b+' itself
            for i in range(1,2):
                if not isinstance(args[i], int):
                    self._error("Addition is only defined for ints.")
                else:
                    total += args[i]
            return IntLit(total)
        elif name == 'b-':
            # TODO: error check first num
            total = args[1]
            if not isinstance(args[2], int):
                self._error("Subtraction is only defined for ints.")
            else:
                total -= args[2]
            return IntLit(total)
        elif name == 'b*':
            total = 1
            for i in range(1,2):
                if not isinstance(args[i], int):
                    self._error("Multiplication is only defined for ints.")
                else:
                    total *= args[i]
            return IntLit(total)
        elif name == 'b/':
            # TODO: err check first num
            total = args[1]
            if not isinstance(args[2], int):
                self._error("Division is only defined for ints.")
            else:
                total /= args[2]
            return IntLit(total)
        elif name == 'b=':
            num = []
            for i in range(1,2):
                if not isinstance(args[i], int):
                    self._error("Number equality is only defined for ints.")
                else:
                    num[i] = args[i]
            if num[1] == num[2]:
                return BoolLit(True)
            else:
                return BoolLit(False)
        elif name == 'b<':
            num = []
            for i in range(1,2):
                if not isinstance(args[i], int):
                    self._error("Number equality is only defined for ints.")
                else:
                    num[i] = args[i]
            if num[1] <= num[2]:
                return BoolLit(True)
            else:
                return BoolLit(False)