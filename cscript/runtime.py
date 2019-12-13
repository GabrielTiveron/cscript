import math
import operator as op
from collections import ChainMap
from types import MappingProxyType

from symbol import Symbol

def eval(x, env):

    if env is None:
        env = ChainMap({}, global_env)

    if isinstance(x, Symbol):
        if isinstance(x, list) and len(x) > 1:
            l = []
            for a in range(len(x)):
                l.append(env[a])
            return l
        return env[x]
    elif isinstance(x, (int, float, bool, str)):
        return x


    if x == None:
          return x
    elif isinstance(x, list):
          if isinstance(x[0], list):
            x = x[0]

    head, *args = x

    if head == Symbol.ADD:
        x,y = args
        return eval(x, env) + eval(y, env)

    elif head == Symbol.SUB:
        x,y = args
        return eval(x, env) - eval(y, env)

    elif head == Symbol.MUL:
        x,y = args
        x = eval(x, env)
        y = eval(y, env)
        return x * y

    elif head == Symbol.DIV:
        x,y = args
        return eval(x, env) / eval(y, env)

    elif head == Symbol.POW:
        x, y = args
        return eval(x, env) ** eval(y, env)

    elif head == Symbol.BLOCK:
        if isinstance(args, list):
            args = args[0]
        for exp in args:
              value = eval(exp, env)
        return value

    elif head == Symbol.IF:
        (_, test, then, *alt) = x
        if alt != []:
            exp = (then if eval(test, env) else None)
            if exp != None:
                value = eval(exp, env)
                return value
            else:
                for i in range(len(alt)):
                    exp = (then if eval(alt[i], env) else None)
                    if exp != None:
                        value = eval(exp, env)
                        return value

        else:
            exp = (then if eval(test, env) else None)
            if exp != None:
                value = eval(exp, env)
                return value

    elif head == Symbol.EQ:
        x, y = args
        return eval(x, env) == eval(y, env)
    
    elif head == Symbol.NEQ:
        x,y = args
        return eval(x, env) != eval(y, env)

    elif head == Symbol.LE:
        x, y = args
        return eval(x, env) <= eval(y, env)

    elif head == Symbol.LT:
        x, y = args
        return eval(x, env) < eval(y, env)

    elif head == Symbol.GT:
        x, y = args
        return eval(x, env) > eval(y, env)

    elif head == Symbol.GE:
        x, y = args
        return eval(x, env) >= eval(y, env)

    elif head == Symbol.DEFINE:
        (_, symbol, exp) = x
        env[Symbol(symbol)] = eval(exp, env)

    elif head == Symbol.TERN:
        var, condition, if_true, if_false = args
        if eval(condition, env):
            env[Symbol(var)] = eval(if_true, env)
        else:
            env[Symbol(var)] = eval(if_false, env)

    elif head == Symbol.FOR:
        assign, condition, expr, block = args
        d = {}
        eval(assign, d)
        value = 0
        while(eval(condition, ChainMap(env, d))):
            value = eval(block, ChainMap(env, d))
            eval(expr, ChainMap(env, d))
        env = ChainMap(env, d)
    
    elif head == Symbol.WHILE:
        condition, block = args
        while(eval(condition, env)):
            value = eval(block, env)

    elif head == Symbol.FUNC:
        name, *arg, block = args
        d = ChainMap()
        if not isinstance(arg, list):
            arg = [arg]
        def fn(*x):
            x = list(x) 
            if isinstance(x, list): 
                x = x[0] 
            for i in range(len(arg[0])):
                d[Symbol(arg[0][i])] = eval(x[i], ChainMap(d))
            return eval(block, ChainMap(d))
        env[Symbol(name)] = fn
        d[Symbol(name)] = fn
        

    elif head == Symbol.CALL:
        name,*arg = args
        return env[Symbol(name)](*arg)

    else:
        raise TypeError
