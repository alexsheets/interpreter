The scheme interpreter will be implemented as a bunch of mutually recursive functions
called eval for evaluating an expr.
When implementing a function call, we'll call a method apply which takes the function
and a list of arguments and applies the function to the arguments; so eval and apply
are mutually recursive.
Code structure is similar to pretty printer:
    - each of the classes in the two hierarchies, you have an eval method
    - and there are three new classes in Node hierarchy for representing environment data structure and closure and builtin
    - closure used for representing functions that were implemented as scheme code
    - builtin for functions that are implemented as python code; primitive builtin functions like car, cdr etc. which interpreter must implement manually.
    - for classes closure and builtin use apply to apply function and everywhere else there is eval for evaluating expression.

- instead of printing what parser returns, we will get what parser returned, feed to interpreter, then the interpreter returns result and main prints it; splice call to interpreter between parsing and pretty printing.
- the eval library function takes some code as argument: think this way
(eval '(+ 2 3) (interaction-environment))
    - you will have method where code itself is the obj. on which you call eval method
    - eval method takes env as arg
    - evaluates result

CLASS HIERARCHY NOTES
- two methods, apply and eval in class node, implementedin each method in node hierachy and special and each class of node and special hierarchy
- apply we have implementation in class node 
- three new classes builtin, environment and closure and apply is in builtin and closure
- the eval method for all the classes in the node hierarchy is essentially a one-liner
- for integer literals, bool literals, and string literals, balance simply referred self
- for nil, builtin, closure and environment, eval should report an error; easiest way of implementing is letting node eval record an error.
- cons, eval, like with print call special eval and ident eval looks up the identifier in the env.
- the magic happens in special hierarchy: lambda and quopte eval are essentially one-liners except quote should have more error handling instead of one-liner
- begin, if, cond, let, set, define implement corresponding special forms
- the regular eval represents the caller side of a function call and apply in builtin and closure implements the callee side of func. calls
- builtin represents builtin funcs represented as python code, closure is for scheme code, environment objects are used for implementing the environment data structure


BUILTIN FUNCTIONS:
- provided a list of builtin functions which interpreter should implement
- the following calls will call parts of the interpreter:
    - read calls the parser and returns parse tree; can raed arbitrary expr.
    - write and display call pretty-printer; prints double quotes around strings so for display keep track of a global variable when calling display it is set; then add a stringlet and do something so printed without quotes...
    - eval calls python eval() function
    - apply calls python apply() function
    - interaction-environment returns a pointer to interpreter's global environment
    - load contains a read-eval loop similar to the one in main script

PROJECT ENVIRONMENT:
- conceptually, an environment is a mapping from identifiers to the values of those idents.
- environment is like hash table; identifiers are hashed, and as a value for each ident. you have the value stored in the environment
- a single table won't be enough, because we have nested functions/functions can access from surrounding funcs and so on; at any given point in time you have a stack of environment objects, inside of this there is a field called scope which points to another node, and a field called env which points to another environment object.
    - the env pointer is the pointer to the surrounding environment
    - the scope pointer is the table stored internally; it is in a peculiar data structure called an association list
    - in handout there is a lengthy explanation abt. environments and their implementation in scheme
    - he implemented part of the environment data structure, and implemented lookup using data structure (association list)
    - the field scope inside an environment points to one such association list implemented using cons nodes
    - assign can be implemented like lookup except modify rather than viewing, define simply adds new definition to local scope.
    - the function at runtime is expressed as closure with lambda, in OOL we see it as closure object containing two pointers: one to lambda expression and one to the environment (written in handout as ...)
    - for our interpreter: each environment object contains an association list for local scope, and instead of a pointer to next list, we have a different list structure
    - ALL ENV CALLS:
    - there is builtin environment, created in main before while loop; add definitions for builtin functions. when main loads ini.scm, those definitons will also be added to builtin environment; then main creates top-level environment, which contains scheme definitions that you enter at scheme prompt; it goes into while loop (passed as arg to eval method calls inside while loop)
    - when you call a function, you create a new env object as well as for a let expression
- tree package, class env:
    - there is a print method which prints the content of environment
    - there are are find and lookup methods
    - at runtime, we have chain of env objects, the innermost env. object and then with the in field inside environment (pointer to surrounding env): find will find an identifier inside the local scope, returns pointer to the cons node that contains the identifier value pair
    - lookup iterates through list of environments, calls find on local env and if it is found it calls getCar to return the value; if not, recursively calls lookup env until it reaches builtin, if not found there it returns an error
    - assign should be implemented the same way (recursive structure, instead of getCar use setCar)
    - define should logically be implemented like:
        - if definition exists, assign new value for this definition
        - else, if not existing, new definition added
        - the easiest way to implement with our data structure is always add new definition to the beginning, functionally this works
    

EVAL METHOD VIDEO:
- for getting started with writing interpreter:
    - write eval methods for Node classes
    - implement all the 'trivial' cases first
        - constants, error cases, test them
        - then, implement Cons and some cases in Special hierarchy

- Node.py: getCar and getCdr return error if not a pair
    - eval: add other definitions
    - takes single argument, an environment;
        - from Tree import Nil stays here
    - apply needs to be added in
- when eval is inherited in class cons, inside cons we will call eval on the special form object; in special hierarchy, eval has two parameters; cons node itself and the environment
- code example: node hierarchy
class IntLit(Node):
    def eval(self, env):
        // integer const returns itself
        return self
        // similar for bool lit, string lit

class Ident(Node):
    // implement environment first
    def eval(self, env):
        return env.lookup(self)

for classes Nil, BuiltIn, Closure, Environment: it doesn't make sense to return anything, report an error
- already code for implementing error in the Node class
- eval got called in something on which it shouldn't have been
- inherit that implementation from Node in those four classes, or have speciailized error messages

class Cons(Node):
    def eval(self, env):
        return form.eval(self, env)


class Quote(Special):
    // exp is cons node passed from cons.eval
    def eval(self, exp, env):
        return exp.getCdr().getCar() except error checks
        - example: don't call getCar if getCdr has nothing

class Lambda(Special):
    def eval(self, exp, env):
        return Closure(exp, env)

// the others will get a bit more complicated

class Regular(Special):
    # if the regular exp is of form (f x y)
    # it needs to evaluate all the expressions
    # eval f: Closure c
    # eval x: 2
    # eval y: 3
    #
    # calls apply on whatever f evaluates to (closure or builtin)
    # call apply passing list of evaluated args, apply does rest of # function call
    # if builtin apply, it will go through if else chain to implement builtin operation within OOL
    # if closure, then closure apply performs function call creating new env object with new parameters, initializing the parameters with values 2 and 3 and calling eval on the function body.
    # c.apply( (2 3) )

- begin, cond, if, let, set all implement corresponding special forms.
- regular eval implements caller side of a function call
- apply in builtin and closure implements the callee side of function calls
- builtin represents builtin funcs added as python code
- closure reps funcs as scheme code
- env objects used for implementing environment structure



ENVIRONMENT IMPLEMENTATION NOTES:
- approach by implementing simple eval; then implement the eval methods in classes begin and if and lambda (one liner)
- at that point, work with constant expressions (if with constants, begin with constats)
- after, implement environment
    - whether use his of using __find and lookup and implementing define and assign to use same data structure/association list
    - or rip it out and implement it using python dictionary
- implement define method of class env first for variable definitions first; then in main after builtin.setenv
- we would add some env.define(ident(x), intlit(7)) and so on so that we could manually populate the environment, and then test it using the interpreter
by implementing lookup for identifiers; implement eval in class ident and see if you get the right values. Then you can add additional definitions to builtin and test whether lookup and assign work correctly to identify vars in toplevel vs bottom level.
- after, implement define eval for var. definitions and implement set eval for assignment and test everything together.

- in debugger at any point, we could put a print call
    - you could take the environment passed and call env.print or any other value .print to pretty print the value
- environment class made available contains isEnvironment, print (for debugging purposes), find (finds variable in local env object), lookup (looks up
value of var, if not in local then looks it up in parent env)

;; builtin env
b+
b*
car
...

;; top-level
(define x 6)
(define y 7)
env can be constructed like this:
((y 7) (x 6))
- easiest way to build list is starting with empty env. and adding each definition in front of the env
- inside an env object, it has two pointers; a pointer to local table and a pointer to the parent env
    - inside top-level env object, we have a local table implemented as a list
    - then, another pointer to the builtin env object
    - Cons(Cons(Ident("y"), Cons(IntLit(7), Nil.getInstance()))

- __find will look for an identifier inside an association list; this is the local list that contains the bindings which say y=7 and x=6
    - if it is not found, it returns None
    - if it does exist, return the Cdr of the binding (because if we look up value of y, we return the Cdr cons node from above)

- lookup gets a value from __find and calls getCar(); we get the IntLit 7 out of the cons node by doing so.
- find only finds it in the local scope; lookup says if find returns None and we have a parent env, then we simply call find on the parent environment
    - say, looking up b*; it isn't in top-level, so we call lookup and find b* in builtin env
    - once __find returns None and there is no surrounding env, we are in builtin env and we report an error saying it is an undefined var.

- we must implement DEFINE and ASSIGN:
- assign needs same code structure as lookup, but instead of getCar, you use setCar
    - assigning a new value to an existing variable means we must look for an existing definition of that var
    - once we find it, we modify the value
- define
    - if we look at scheme definition, if the definition for a var already exists/we have prev defined 'id' in current env, then we assign a new value to it
    - else, we add a new definition

(define x 3)
- using find, we look for existing value x; we modify it and put the new value there
- if we don't find it, then we add a new definition to front; you can possibly just do this because next time you look it up you will just find the new
value and not the old one. This causes a memory leak and the old storage for x is no longer reachable.
- this makes implementing var definitions easy because you simply call define on env and then put a new defintion in front

- this is what env itself does, this is the way the calls are made:
    - lookup on env that is made in ident eval
    - assign would call setEval for class set
    (set! x 3) --> the new value that should be assigned to x should be an arbitrary exp; the value is passed to assign method of class env
    - the variable itself (x) shouldn't be evaluated becuase we are interested in the var
    - same goes for variable definitions
    (define x 3) --> the 3 is an arbitrary exp evalauted first, before we call define on env to add definition to say x has value of this expression

    (define (f x) x) --> equivalent to (define f (lambda (x) x))
    - so for func definition implementation of define, extract the parameter list, extract body of function, then construct lambda expression using that
    - just like before, lambda (x) x is the arbitrary exp to evaluate; this will return a closure which is added as a variable f in the environment.


BUILTIN FUNCTIONS:
    - list of builtin functions to be implemented:
        - symbols, 32 bit ints, booleans, strs, lists, closures (data structures)
        - symbol? for identifying an ident
        - number? for identifying integers and the binary arithmetic operations b+, b-, b*, b/, b=, b<
        - list operations car, cdr, cons, set-car!, set-cdr!, null?, pair?, eq?
        - procedure? for identifying closure or built-in function
        - the I/O functions read, write, display, newline (without port)
            - read reads an entire expression, write writes an entire one, display is diff. because any strings with double quotes will be written without
            - read calls the parser and returns a parse tree
            - write and display call pretty printer
        - functions eval, apply, interaction-environment
            - eval is builtin function which runs interpreter; for executing eval builtin function we call eval method of our interpreter and similarly for apply and interaction environment returns a pointer to our top level env
            - eval and apply call their respective python function
            - interaction-env returns a pointer to the interpreter's top level global env
        - function load
            - takes a file main as arg, opens an input stream from that file, then reads and evaluates all the scheme exps inside (used for loading a startup file ini.scm)
            - read-eval loop similar to the one in main


IMPLICIT BEGIN/LET/COND:
