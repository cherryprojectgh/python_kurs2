source = 'report_line += 1'
import time

report_line = 0


start = time.time()
for _ in range(10):
    exec(source)
stop = time.time()
time_not_compiled = stop - start
print(time_not_compiled)

start = time.time()
source_compiled = compile(source, 'internal variable source', 'exec')
for _ in range(10):
    exec(source_compiled)
stop = time.time()
time_compiled = stop - start
print(time_compiled)

print()

#------------------------------------------------------------------------------------------------

import math
import time
 
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
 
argument_list = []
 
 
for i in range (1000000):
    argument_list.append(i/10)
 
for formula in formulas_list:
 
    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))
 
    
for formula in formulas_list:
 
    results_list = []
    print("Formula {}".format(formula))
    
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    
    print("Calculation time: {}".format(stop - start))