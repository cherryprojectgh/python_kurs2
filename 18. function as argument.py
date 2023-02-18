def bake(what):
    print('Baking {}'.format(what))

def add(what):
    print('Adding {}'.format(what))

def mix(what):
    print('Mixing {}'.format(what))

cookbook = [(add, 'milk'),(add, 'eggs'),(add, 'sugar'),(mix, 'ingredients'),(bake, 'cookies')]

for activity, obj in cookbook:
    activity(obj)

print('-'*30)

def cook(activity,obj):
    activity(obj)

cook(bake, 'brownies')

for activity, obj in cookbook:
    cook(activity,obj)

print('-'*30)
#------------------------------------------------------------------------------------

def double(x):
    return 2*x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2


def generate_values(function, list):
    for element in list:
        print(function(element))

x_table = list(range(11))
print(x_table)
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))
