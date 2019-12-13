






# binop
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

#if
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
