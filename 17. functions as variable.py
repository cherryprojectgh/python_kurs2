#zmienna może być funkcją. Po przypisaniu funkcji do zmiennej, zmienna działa jak funkcja

def buy_me(what):
    print('Give me ', what)

buy_me('a new car')

steal_for_me = buy_me
print(type(steal_for_me))

#------------------------------------------------------------------
def double(x):
    return 2*x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8
transformations = [double, square, div2, negative]
tmp_return_value = number

for element in transformations:
    tmp_return_value = element(tmp_return_value)

print('Wychodzi ', tmp_return_value)