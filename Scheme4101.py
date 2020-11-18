# Scheme4101 -- The main program of the Scheme interpreter

import sys
from Parse import *
from Tokens import TokenType
from Tree import StrLit
from Tree import Ident
from Tree import Cons
from Tree import TreeBuilder
from Tree import BuiltIn
from Tree import Environment
from Tree import Closure
from Special import Special
from Util import Util

if __name__ == "__main__":
    # Initialization file with Scheme definitions of built-in functions
    ini_file = "ini.scm"

    prompt = "> "

    # Create scanner that reads from standard input
    scanner = Scanner(sys.stdin)

    util = Util()
    Cons.setUtil(util)
    BuiltIn.setUtil(util)
    Closure.setUtil(util)
    Special.setUtil(util)

    if (len(sys.argv) > 2 or
        (len(sys.argv) == 2 and sys.argv[1] != "-d")):
        sys.stderr.write("Usage: python3 SPP.py [-d]\n")
        sys.stderr.flush()
        sys.exit(2)

    # If command line option -d is provided, debug the scanner.
    if len(sys.argv) == 2 and sys.argv[1] == "-d":
        tok = scanner.getNextToken()
        while tok != None:
            tt = tok.getType()

            sys.stdout.write(str(tt))
            if tt == TokenType.INT:
                sys.stdout.write(", intVal = " + str(tok.getIntVal()) + "\n")
            elif tt == TokenType.STR:
                sys.stdout.write(", strVal = " + tok.getStrVal() + "\n")
            elif tt == TokenType.IDENT:
                sys.stdout.write(", name = " + tok.getName() + "\n")
            else:
                sys.stdout.write("\n")
            sys.stdout.flush()

            tok = scanner.getNextToken()
    else:
        # Create parser
        builder = TreeBuilder()
        parser = Parser(scanner, builder)

        # creating empty builtin environment
        env = Environment()

        builtins = ['car', 'cdr', 'cons', 'set-car!', 'set-cdr!', 'null?', 'pair?', 'eq?', 'symbol?', 'number?', 'procedure?', 'read', 'write', 'display', 'newline',
                    'eval', 'apply', 'interaction-environment', 'load']
        for builtin in builtins:
            iden = Ident(builtin)
            env.define(iden, BuiltIn(iden))

        # env = Environment(env)

        # load all definitions from ini.scm
        # add them to builtin env
        # eventually, create top level environment which points to builtin environment as its surrounding environment

        # then code where you would read init.scheme file

        # so that when you populate the environment for loading ini.scm, that class Builtin knows where to find builtin env
        BuiltIn.setEnv(env)
        ### need to write which essentially does the car/ident thing and reads ini.scm file
        ### for both adding the builtin functions and then load the ini.scm
        # Environment.populateEnv(env, ini_file)
        env = Environment(env)
        # so it knows where to find toplevel for interaction environment
        BuiltIn.setEnv(env)

        # Read-eval-print loop

        sys.stdout.write(prompt)
        sys.stdout.flush()
        root = parser.parseExp()
        while root != None:
            # env here is the toplevel env
            root.eval(env).print(0)
            sys.stdout.write(prompt)
            sys.stdout.flush()
            root = parser.parseExp()


# WHAT HAPPENS WITH FUNCTION CALLS
# (define (add x) (lambda (y) (b+ x y)))
# (define n 1)
# (define add1 (add n))
# (define i (add1 10))


# Cons.eval
#   Regular.eval (add)
#       Ident.eval
#           f = Closure((lambda (x) (lambda (y) (b+ x y))), env)
#       Ident.eval
#           a = 1
#       f.apply( (a) )
#           fenv = new Environment(env)
#           fenv.define(x, 1)

# Stack:
# main:
#   add
#   n = 1
#   add1 = 
# add1:
#   y = 10