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
        .replace('\n', '')\
        .replace('(', ' ( ').replace(')', ' ) ')
    
    return source_string


def tokenize_source (source_string):
    """Tokenize a valid quickLi expression string with spaces between
    every symbol (procedures and operands built-in or otherwise).

    NOTE: EOF and null-terminators are not necessary, abstracted away by load_source function. 

    :param source_string: quickLi expression string
    :type source_string: str
    :return: 'stream' (list) of valid tokens ready to be parsed     
    """
    tokens = source_string.split()
    lexer = re.compile(
        r"""\s*(,@|[('`,)]|"(?:[\\].|[^\\"])*"|;.*|[^\s('"`,;)]*)(.*)"""
    )
    return tokens



    



source = '''
(begin 
    (define nth (lambda (n l)
        (if (null? l) nil
        (if (eq? n 0) (car l) (nth (- n 1) (cdr l))))))
    
    (define combine (lambda (proc)
        (lambda (x y)
            (if (null? x) (quote ())
                (proc (list (car x) (car y))
                    ((combine proc) (cdr x) (cdr y)))))))
    (define zip (combine cons))

    (define inter (lambda (l1 l2)
        (cond ((null? l1) nil) 
              ((member? (car l1) l2) 
                (cons (car l1) (inter (cdr l1) l2)))
              (inter (cdr l1) l2) )))

    ;; linear recursion, quite slow and will grow the stack 
    ;; arbitrarily if you do not use tail calls
    (define slow-reverse (lambda (l)
        (if (null? l) nil 
        (+ (slow-reverse (cdr l)) (cons (car l) nil)))))



    ;; much faster implementation using an accumulator
    ;; and a tail recursive procedure call
    ;; (with tail call, we do not have to wait for the child routines to converge)
    (define fast-reverse (lambda (l a)
        (if (null? l) a
        (fast-reverse (cdr l) (cons (car l) a)))))

    (fast-reverse (list 1 2 3 4 5 6 7 8 9 1 2 4 5 6 7) nil)
)
'''
test = load_source(source, file=False)
toks = tokenize_source(test)
print(toks)