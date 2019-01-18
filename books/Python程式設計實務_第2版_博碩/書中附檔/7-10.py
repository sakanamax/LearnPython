# 程式7-10.py ( Python 3 version )

import sympy
a, b = 500,600
numbers = range(a,b)
prime_numbers = filter(sympy.isprime, numbers)
print("Prime numbers({}-{}):".format(a,b))
print(",".join(map(str,prime_numbers)))
