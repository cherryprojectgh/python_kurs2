import itertools as it

myList = ['a','b','c','d']

for combination in it.combinations(myList, 3):
    print(combination)

print('-'*100)

for combination in it.permutations(myList, 3):
    print(combination)

print('-'*100)

for combination in it.combinations_with_replacement(myList, 3):
    print(combination)


import math
 
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
 
for x in it.permutations(notes, 4):
    print(x)
 
print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))
 
input('Press enter')
 
for x in it.product(notes, repeat=4):
    print(x)
 
print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))