from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol

class CscriptTransformer(InlineTransformer):

    number = float
    name = str
    
    def binop(self, left, op, right):
        op = str(op)    
        return (op, left, right)

    def symbol(self, symbol):
        return Symbol(symbol)
      
    def cmd(self, *args):
        return ('cmd', *args)
    
    def assign(self, left, op):
        return(Symbol.ASS, left, op)

    def binop(self, *args):
        return(args)
    
    def sum(self, left, right):
        print('@@@@@@@@@@@@@@@@@@@@', left, right)
        return list(tuple((Symbol.ADD, left, right)))
    
    def sub(self, left, right):
        return(Symbol.SUB, left, right)
    
    def mul(self, left, right):
        return(Symbol.MUL, left, right)

    def div(self, left, right):
        return(Symbol.DIV, left, right)

    def pow(self, left, right):
        return(Symbol.POW, left, right)

    def bool(self, boolean):
        return boolean == True

def parse(src: str):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)

def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """

    path = Path(__file__).parent / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=CscriptTransformer())
    return grammar

parser = _make_grammar()
