# TreeBuilder -- Abstract Factory for building tree node objects

from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons

class TreeBuilder:
    def __init__(self):
        pass

    def buildBoolLit(self,b):
        return BoolLit.getInstance(b)

    def buildIntLit(self,i):
        return IntLit(i)
                            
    def buildStrLit(self,s):
        return StrLit(s)

    def buildIdent(self,n):
        return Ident(n)

    def buildNil(self):
        return Nil.getInstance()

    def buildCons(self,a, d):
        return Cons(a, d)

if __name__ == "__main__":
    i = TreeBuilder().buildIntLit(42)
    i.print(0)
