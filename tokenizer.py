"""
Purpose
--------
This module holds the required types and functions to lexically analyze
a quickLi expression in the form of a string (file or otherwise). Employing
regex to minimize code. Note, a quickLi program is actually one quickLi expression.
This means the notion of 'lines' is abstract and of no concern to the compiler, so
long as whitespace is used between procedures and operands. These abstract lines
are determined by the use of line-break in the source string. Additionally, there
are zero syntax exceptions.
"""
import sys, os, re


def load_source (reference, file=True):
    """Read quickLi expression from given reference. Could be file path or string.

    NOTE: Ignores lines beginning with ';' as comments.
    
    :param reference: where to find quickLi expression string
    :param file: indicates nature of reference (file path or string)
    :type file: bool
    :type reference: str
    :return: source string to be tokenized
    """
    lines = []
    if file:
        # process file off disk into memory
        if os.path.isfile(reference): lines = open(reference).readlines()
        else:
            sys.exit('[!] quickLi: file not found')
    else:
        lines = reference.split('\n')

    # format the 'lines' of the quickLi expression (redundant replace calls?)
    source_string = ' '.join([l.strip() for l in lines if ';' not in l and not (l.isspace() or l == '')])\
        .replace('\t', '')\
        .replace('\n', '')
    
    return source_string


def tokenize_source (source_string):
    """Tokenize a valid quickLi expression string with spaces between
    every symbol (procedures and operands built-in or otherwise) by seperating
    surrounding parenthesis and stepping through each element.

    NOTE: EOF checks are not necessary, abstracted away by load_source function.

    :param source_string: quickLi expression string
    :type source_string: str
    :return: 'stream' (list) of valid tokens ready to be parsed     
    """
    tokens = source_string.replace('(', ' ( ').replace(')', ' ) ').split()
    formatted_tokens = []
    lexer = re.compile(
        r"""\s*(,@|[('`,)]|"(?:[\\].|[^\\"])*"|;.*|[^\s('"`,;)]*)(.*)"""
    )

    return tokens



source = '''(begin

                        (add 1 2)

  )





'''
test = load_source(source, file=False)
toks = tokenize_source(test)
print(toks)