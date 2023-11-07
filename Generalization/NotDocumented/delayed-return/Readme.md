# Delayed return vs. direct return

In some older languages (as C) it was good style to have the result
(return value) defined as a variable and then return this at the end
of the function.  Since the object orientated paradigm is out, and
using a language that this supports, this type of handling is not
needed.

Code:

    res = None
    if a:
	   res = 7
	else:
	   res = 9
	return res

vs.

    res = None
    if a:
	   return 7
	else:
	   return 9
	   
Bytecode sizes:

* direct return: 26
* delayed return: 20

Direct return in this case is about 10% faster.
