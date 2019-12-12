from lark import Lark


cscript = Lark(r"""
?start : (block)+

?block : expr (";" expr)*

?expr : assign
      | term
      | if
      | func
      | loop
      | "(" expr ")"

?term : value
      | binop
      | call

?func : "func" value "(" value ("," value)* ")""{"  block "}"

call : value "(" expr+ ("," expr+)*")"

?if : "if" "(" condition ")" "{" block "}" else_if* else? -> if_cond
    | expr "=" condition "?" expr ":" expr -> ternario

?else_if : "else if" "(" condition ")" "{" block "}"

?else : "else" "{" block "}"

?loop : "for" "(" assign ";" condition ";" expr ")" "{" block "}" -> for_loop
      | "while" "(" condition ")" "{" block "}" -> while_loop

?condition : expr "==" expr -> eq
           | expr ">=" expr -> goeq
           | expr "<=" expr -> lesseq
           | expr ">" expr  -> gt
           | expr "<" expr  -> lt
           | expr

?binop : expr "+" expr -> sum
       | expr "-" expr -> sub
       | expr "*" expr -> mul
       | expr "/" expr -> div
       | expr "^" expr -> pow

?assign : value "=" term

?value : STRING -> string
       | INT -> number
       | FLOAT -> number
       | BOOLEAN -> bool
       | NAME -> name
       | SYMBOL -> symbol



// Terminais
BOOLEAN : /[TF]/
NAME    : /[a-zA-Z]\w*/
SYMBOL  : /[-!+\/*@$%^&~<>?|\\\w]+/
STRING  : /"[^"\\]*(\\[^\n\t\r\f][^"\\]*)*"/
INT     : /-?\d+/
FLOAT  : /-?\d+\.\d+/


%ignore /\s+/
%ignore /\n/
%ignore /\/\/[^\n]*/
""")
