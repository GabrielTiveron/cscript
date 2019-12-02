from lark import Lark, InlineTransformer
from pathlib import Path

from .runtime import Symbol

class LispTransformer(InlineTransformer):

    number = float
    name   = str

    def start(self, *args):
        return list(args)

    def value(self, op, value):
        op = Symbol(op)
        return list(op, value)

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
        grammar = Lark(fd, parser='lalr', transformer=LispTransformer())
    return grammar

parser = _make_grammar()
