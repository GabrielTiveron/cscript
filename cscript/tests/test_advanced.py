from lispy import var, env, Symbol, parse, eval

run = lambda src, env=None: eval(parse(src), env)
x, y, a, b, c, f, g, h, op = map(Symbol, 'x y a b c f g h op'.split())


class TestRuntime:
    def test_eval_quote(self):
        assert run("'\"string\"") == "string"
        assert run("'if(true) 42; 0;)") == run("if(true) 42; else 0;") == [Symbol.IF, True, 42, 0]

