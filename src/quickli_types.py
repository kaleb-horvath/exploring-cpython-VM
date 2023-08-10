"""
Purpose
--------
quickLi types used by the parser.
"""
symbol_type = str 
number_type = (int, float)
boolean_type = (False, True)
list_type = list 

# primitive special forms
symbol_define = symbol_type('define')
symbol_lambda = symbol_type('lambda')
symbol_if = symbol_type('if')
symbol_set = symbol_type('set!')
symbol_quote = symbol_type('quote')
symbol_begin = symbol_type('begin')
symbol_cond = symbol_type('cond')


# primitive procedures (regular forms?)