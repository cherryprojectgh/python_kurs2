# funkcja id() zwraca id  zmiennej w pamięci
# operator is sprawdza czy podane zmienne sa tym samym obiektem w pamięci

print()

a=b=c=10

print(a,id(a),b,id(b),c,id(c))

a = 20

print(a,id(a),b,id(b),c,id(c))

#---------------------------------------------------------------------------------------

print()

aa = [1,2,3]
bb = aa
cc = aa

print(aa,id(aa),bb,id(bb),cc,id(cc))

aa.append(4)

print(aa,id(aa),bb,id(bb),cc,id(cc))

#---------------------------------------------------------------------------------------

print()

x = 10
y = 10

print(x,id(x),y,id(y))

y = y + 1 - 1

print(x,id(x),y,id(y))