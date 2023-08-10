"""
Purpose
--------
This module holds the required types and functions to lexically analyze
a quickLi expression in the form of a string (file or otherwise). Employing
regex to minimize code. 
"""
import sys, os, re


def load_source (reference, file=True):
    """Read quickLi expression from given reference. Could be file path or string.

    NOTE: Ignores lines beginning with ';' as comments.
    
    :param reference: where to find quickLi expression string
    :param file: indicates nature of reference (file path or string)
    :type file: bool
    :type reference: str
    :return: lines of the quickLi program/expression
    """
    lines = []
    if file:
        # process file off disk into memory
        if os.path.isfile(reference): lines = open(reference).readlines()
        else:
            sys.exit('[!] quickLi: file not found')
    else:
        lines = reference.split('\n')



def tokenize_source (lines):
    """Ingest list of lines of a quickLi program/expression.
    Convert lines to a valid quickLi expression string with spaces between
    every symbol (procedures and operands built-in or otherwise), and then
    tokenize.

    NOTE: EOF and null-terminators are not necessary, abstracted away by load_source function. 

    :param lines: lines of the quickLi program/expression
    :type lines: list
    :return: 'stream' (list) of valid tokens ready to be parsed     
    """

    # format the 'lines' of the quickLi expression (redundant replace calls?)
    return ' '.join([l.strip() for l in lines if ';' not in l and not (l.isspace() or l == '')])\
        .replace('\t', '')\
        .replace('\n', '')\
        .replace('(', ' ( ').replace(')', ' ) ').split()

    # attempts to handle string literals for later
    #lexer = re.compile(
    #    r"""\s*(,@|[('`,)]|"(?:[\\].|[^\\"])*"|;.*|[^\s('"`,;)]*)(.*)"""
    #)


