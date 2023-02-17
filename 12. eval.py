var_x = 10
password = 'My super secret password'

source = 'password'

#globals = globals().copy()
#del globals['password']
globals = {}

result = eval(source, globals)
print(result)

print(globals())

#-------------------------------------------------------------------

import math
 
argument_list = []
 
for i in range (100):
    argument_list.append(i/10)
    
formula = input("Please enter a formula, use 'x' as the argument: ")
 
for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))