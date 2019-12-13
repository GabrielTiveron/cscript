from lark import Lark, InlineTransformer
from pathlib import Path

from runtime import Symbol
from grammar import cscript

class CscriptTransformer(InlineTransformer):

    number = float
    name = str

    def start(self, *block):
        return list(tuple((list(block))))

    def binop(self, left, op, right):
        op = str(op)
        return (op, left, right)

    def block(self, *block):
        block = list(block)
        return list(tuple((Symbol.BLOCK, block)))

    def name(self, name):
        return Symbol(name)

    def symbol(self, symbol):
        return Symbol(symbol)

    def string(self, string):
        return list(tuple((string[1:-1])))

    def assign(self, left, op):
        return list(tuple((Symbol.DEFINE, Symbol(left), op)))

    def binop(self, *args):
        return(args)

    def condition(self, *args):
        return args

    def func(self, *args):
        name, *params, body = args
        lis = []
        for param in params:
            lis.append(param)
        return list(tuple((Symbol.FUNC, name, lis, body)))

    def call(self, *params):
        name, *param = params
        return list(tuple((Symbol.CALL, name, list(param))))

    def if_cond(self, condition, exp, *else_if):
      lis = []
      for arg in else_if:
          lis.append(arg)
      if lis != []:
          return list(tuple((Symbol.IF, condition, exp, lis)))
      else:
          return list(tuple((Symbol.IF, condition, exp)))

    def sum(self, left, right):
        return list(tuple((Symbol.ADD, left, right)))

    def sub(self, left, right):
        return list(tuple((Symbol.SUB, left, right)))

    def mul(self, left, right):
        return list(tuple((Symbol.MUL, left, right)))

    def div(self, left, right):
        return list(tuple((Symbol.DIV, left, right)))

    def pow(self, left, right):
        return list(tuple((Symbol.POW, left, right)))

    def bool(self, boolean):
        return Symbol(boolean) == Symbol.TRUE

    def lt(self, left, right):
        return list(tuple((Symbol('<'), left, right)))

    def gt(self, left, right):
        return list(tuple((Symbol('>'), left, right)))

    def eq(self, left, right):
        return list(tuple((Symbol('=='), left, right)))

    def lesseq(self, left, right):
        return list(tuple((Symbol('<='), left, right)))

    def goeq(self, left, right):
        return list(tuple((Symbol('>='), left, right)))

    def ternario(self, var, condition, if_true, if_false):
      return list(tuple((Symbol.TERN, var, condition, if_true, if_false)))

    def else_if(self, condition, exp):
        return list(tuple((condition, exp)))

    def for_loop(self, assign, condition, expr, block):
        return list(tuple((Symbol.FOR, assign, condition, expr, block)))

    def while_loop(self, condition, block):
        return list(tuple((Symbol.WHILE, condition, block)))

def parse(src: str):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parse(src)


parse = cscript.parse
