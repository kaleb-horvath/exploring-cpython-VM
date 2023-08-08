# quickLi
a super quick language implementation eerily similar to such languages as Lisp and Scheme. entirely for my own convenience. this package compiles quickLi source code strings down to  CPython bytecode, the powerful stack-machine based instruction set. from here, the user has the option to invoke the Python runtime over the 'object file' or make use of the quickLi wrapper (occurs when using the repl).

*the compiler itself is written in Python in my style which is very procedural. at this stage, the focus is to make it as portable as possible and write the minimum amount of code required to get the implementation off the ground*

### initial objectives
1. working lexer and parser on repl (keeping in mind safety and exception handling)

### future goals
* stack tracing functionality to assist in debugging
* cache-aware parser
* built-in time profile tool
* tail-call optimization to eliminate CPython stack overflow due to excessive recursions
