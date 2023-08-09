# quickLi
a super quick language implementation eerily similar to such languages as Lisp and Scheme. entirely for my own convenience. this package compiles quickLi source code strings down to  CPython bytecode, the powerful stack-machine based instruction set. from here, the user has the option to invoke the Python runtime over the 'object file' or make use of the quickLi wrapper (occurs when using the repl). Note, a quickLi program is actually one quickLi expression. This means the notion of 'lines' is abstract and of no concern to the compiler, so long as whitespace is used between procedures and operands. These abstract lines are determined by the use of line-break in the source string. Additionally, there are only two syntax exceptions. These are to delineate boolean (#t, #f) and the string primitive (`abc i am text`)

*the compiler itself is written in Python in my style which is very procedural. at this stage, the focus is to make it as portable as possible and write the minimum amount of code required to get the implementation off the ground*

### initial objectives
1. Naive lexer and parser on repl (keeping in mind safety and exception handling)

### future goals
* robust regex integration 
* robust logging functionality and error types (sub-class of Exception possibly? pre-set error messages?)
* stack tracing functionality to assist in debugging
* cache-aware parser
* built-in time profile tool
* tail-call optimization to eliminate CPython stack overflow due to excessive recursions
