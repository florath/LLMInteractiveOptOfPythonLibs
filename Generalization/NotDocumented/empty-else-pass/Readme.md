# Empty "else: pass"

Example:

    if i < 1000:
        print(i)
    else:
        pass

versus:

    if i < 1000:
        print(i)


It looks that this eats up space and time. The 'pass' is 
converted into a bytecode "NOP" and needs execution time
and an additional byte.

Bytecode length of the code with the "else: pass" is 26 and
without this is 24.

There is a very small performance improvement of somewhat more than
1%.
