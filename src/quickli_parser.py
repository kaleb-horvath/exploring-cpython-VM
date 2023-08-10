"""
Purpose
--------
This module contains the required types and functionality to parse a stream of quickLi
tokens into an Abstract Syntax Tree. 
"""
import quickli_types 
import sys 

def native_type (token):
    """Convert a quickLi token to a native Python type
    
    :param token: quickLi expression component to convert
    :type token: str
    :return: native casted token
    """
    if token == '#t': return quickli_types.boolean_type[1]
    if token == '#f': return quickli_types.boolean_type[0]
    else:
        try:
            return quickli_types.number_type[0](token)
        except ValueError:
            try:
                return quickli_types.number_type[1](token)
            except ValueError:
                return quickli_types.symbol_type(token)
    

def parse (tokens):
    """Convert token stream into abstract syntax tree.

    :param tokens: collection of quickLi expression tokens
    :type tokens: list
    :return: tree containing native types representing program structure
    """
    #try:
    if len(tokens) == 0: sys.exit('[!] quickLi: no tokens')
    token = tokens.pop(0)

    if token is '(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token is ')': sys.exit('[!] quickLi: expected \'(\' for beginning of expression')
    else:
        return native_type(token)

    #except Exception:
        sys.exit('[!] quickLi: unknown parser failure')

"""  
import quickli_tokenizer
program = quickli_tokenizer.load_source("(begin (+ 1 ( * 1 (/ 10 2))))", file=False)
tokens = quickli_tokenizer.tokenize_source(program)
syntax_tree = parse(tokens)
print(syntax_tree)
"""