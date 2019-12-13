class Symbol:

    data : str
    CACHE = {}

    def __new__(cls, data):
        if isinstance(data, Symbol):
            return data
        try:
            return cls.CACHE[data]
        except KeyError:
            cls.CACHE[data] = new = super().__new__(cls)
            new._data = data
            return new

    def __str__(self):
        return self._data

    def __repr__(self):
        return self._data

    def __hash__(self):
        return id(self._data)

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self._data == other._data
        return NotImplemented

#Definição de Simbolos
Symbol.IF     = Symbol('if')
Symbol.ELSIF  = Symbol('else if')
Symbol.ADD    = Symbol('+')
Symbol.SUB    = Symbol('-')
Symbol.MUL    = Symbol('*')
Symbol.DIV    = Symbol('/')
Symbol.DEFINE = Symbol('=')
Symbol.POW    = Symbol('^')
Symbol.TRUE   = Symbol('T')
Symbol.EQ     = Symbol('==')
Symbol.NEQ    = Symbol('!=')
Symbol.GT     = Symbol('>')
Symbol.LE     = Symbol('<=')
Symbol.LT     = Symbol('<')
Symbol.GE     = Symbol('>=')
Symbol.TERN   = Symbol('?')
Symbol.FUNC   = Symbol('func')
Symbol.CALL   = Symbol('call')
Symbol.FOR    = Symbol('for')
Symbol.WHILE  = Symbol('while')
Symbol.BLOCK  = Symbol('block')
