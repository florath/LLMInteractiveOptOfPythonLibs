# If-Else

This test checks the construct:

	if a:
	    run1()
	else:
		run2()
		
versus:

    if not a:
	    run2()
	else:
		run1()

		
Is the first "run1()" called faster than the second "run2()"?
If e.g. run1() is called much more often. Is there any speed gain?

The size of the bytecode for both is 34. Both implementations
come mostly with the same performance.

(Reading the bytecode: there is always one conditional and one fixed
jump included in both ways.)
