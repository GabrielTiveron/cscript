#from .parser import var, env, Symbol, parse, eval, global_env
from parser import CscriptTransformer
from grammar import cscript
from runtime import eval
from symbol import Symbol    

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, h, op = map(Symbol, 'x y a b c f g h op'.split())


class TestCscriptGrammar:
    #binop
    value_sum = cscript.parse('1 + 2')
    value_sub = cscript.parse('3 - 2')
    value_mul = cscript.parse('12 * 3')
    value_div = cscript.parse('14 / 2')
    value_pow = cscript.parse('2 ^ 10')

    soma = CscriptTransformer().transform(value_sum)
    sub  = CscriptTransformer().transform(value_sub)
    mul = CscriptTransformer().transform(value_mul)
    div = CscriptTransformer().transform(value_div)
    pow_ = CscriptTransformer().transform(value_pow)
    #condicao
    value_if = cscript.parse('if (T){2 + 2} else if (T){2 - 2}')
    value_Eq = cscript.parse('if (2 == 2){1 + 2}')
    value_Gt = cscript.parse('if (3 > 1){3 + 5}')
    value_Le = cscript.parse('if (4 <= 5){2 + 5}')
    value_Lt = cscript.parse('if (3 < 5){3 * 1}')
    value_Ge = cscript.parse('if (3 >= 4){2 ^ 3}')
    value_ternario = cscript.parse('asd = 3 > 0 ? 1 : 2')

    if_if = CscriptTransformer().transform(value_if)
    if_Eq = CscriptTransformer().transform(value_Eq)
    if_Gt = CscriptTransformer().transform(value_Gt)
    if_Le = CscriptTransformer().transform(value_Le)
    if_Lt = CscriptTransformer().transform(value_Lt)
    if_Ge = CscriptTransformer().transform(value_Ge)
    if_ternario = CscriptTransformer().transform(value_ternario)
    #func
    func = cscript.parse('func lambda (a, b, c){a + b - c}')
    call = cscript.parse('lambda(15, 94, 2)')
    eval_func = CscriptTransformer().transform(func)
    eval_call = CscriptTransformer().transform(call)
    #loop
    loop = cscript.parse("""
    a = 2;

    for(x = 3; x <= 10; x = x + 1){
        a = a + x
    };

    a
    """)
    loop_transform = CscriptTransformer().transform(loop)
    #while
    while_p = cscript.parse("""
    a = 1;
    while(a < 10){
        a = a + 1
    }
    """)
    while_trans = CscriptTransformer().transform(while_p)

    def test_binop(self):
        assert soma == [Symbol.ADD, 1.0, 2.0]
        assert sub == [Symbol.SUB, 3.0, 2.0]
        assert mul == [Symbol.MUL, 12.0, 3.0]
        assert div == [Symbol.DIV, 14, 2]
        assert pow_ == [Symbol.POW, 2, 10]

    def test_if(self):
        assert if_if == [Symbol.IF, True, [Symbol.ADD, 2.0, 2.0], [[True, [Symbol.SUB, 2.0, 2.0]]]]
        assert if_Eq == [Symbol.IF, [Symbol.EQ, 2.0, 2.0], [Symbol.ADD, 1.0, 2.0]]
        assert if_Gt == [Symbol.IF, [Symbol.GT, 3.0, 1.0], [Symbol.ADD, 3, 5]]
        assert if_Le == [Symbol.IF, [Symbol.LE, 4.0, 5.0], [Symbol.ADD, 2, 5]]
        assert if_Lt == [Symbol.IF, [Symbol.LT, 3.0, 5.0], [Symbol.MUL, 3, 1]]
        assert if_Ge == [Symbol.IF, [Symbol.GE, 3.0, 4.0], [Symbol.POW, 2, 3]]
        assert if_ternario == [Symbol.TERN, Symbol('asd'), [Symbol.GT, 3, 0], 1, 2]
        env = {Symbol('b'): 2}
        print_ = cscript.parse('b = b == 2 ? 6 : 0')
        print_eval = CscriptTransformer().transform(print_)
        res = eval(print_eval, env)
        assert env[Symbol('b')] == 6

    def test_eval(self):
        assert eval(div, {}) == 7
        assert eval(soma, {}) == 3
        assert eval(sub, {}) == 1
        assert eval(mul, {}) == 36
        assert eval(pow_, {}) == 1024
        assert eval(if_if, {}) == 4
        assert eval(if_Eq, {}) == 3
        assert eval(if_Gt, {}) == 8
        assert eval(if_Le, {}) == 7
        assert eval(if_Lt, {}) == 3
        assert eval(if_Ge, {}) is None
        env = {'asd': 2}
        assert eval(if_ternario, env) == None
        assert env[Symbol('asd')] == 1

    def test_func(self):
        env = ChainMap()
        assert eval(eval_func, env) is None
        assert eval(eval_call, env) == 107

    def test_loop(self):
        print(loop_transform)
        env = {}
        assert eval(loop_transform, env) == 54
        env = {}
        eval(while_trans, env)
        assert env[Symbol('a')] == 10



class TestEnvCreation:
    def test_env_creation(self):
        assert env() == global_env
        assert set(env({var.x: 42})).issuperset(set(global_env))
        assert env({var.x: 42})[var.x] == 42
        assert env(x=42)[var.x] == 42


class TestRuntime:
    def test_eval_simple(self):
        assert run('42') == 42

    def test_eval_if_simple(self):
        assert run('if(T) 42; 0;') == 42
        assert run('if(F) 42; 0;)') == 0

    def test_eval_if_nested(self):
        assert run('if (1 % 2 == 1) 40 + 2; 1 + 1;') == 42
        assert run('if (1 % 2 == 0) 40 + 2; 1 + 1;') == 2

    def test_eval_define_simple(self):
        e = env()
        assert run("x = 42", e) is None
        assert e[Symbol('x')] == 42

    def test_eval_define_nested(self):
        e = env()
        assert run("x = 40 + 2", e) is None
        assert e[Symbol('x')] == 42

    def test_call_environment_functions(self):
        assert run('42 % 2 == 0') is True
        assert run('42 % 2 == 1') is False

    def test_call_function_with_nested_arguments(self):
        assert run('(1 + 1) % 2 == 0') is True
        assert run('2 * 3 + 4') == 10
