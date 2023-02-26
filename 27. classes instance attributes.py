#klasa
class Car:

    #obiekt
    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

#instancja klasy
car01 = Car('Seat','Ibiza',True,True,True)
car02 = Car('Opel','Corsa',True,False,True)

print(car01.brand, car01.model, car01.isAirbagOK, car01.isPaintingOK, car01.isMechanicOK)

#---------------------------------------------------------------------------------------------------

class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind 
        self.taste = taste
        self.additives = additives
        self.filling = filling

lista = ['element1', 'element2']
listaAll = ' '.join(lista)

cake01 = Cake('trufla','ciastko','słodki', listaAll, 'róża')
cake02 = Cake('coś tam','tort','gorzki', listaAll, 'czekoladowy')

print(cake01.name)

bakery_offer = [cake01, cake02]

for e in bakery_offer:
    print('{} - {} main taste: {} with additives of {}, filled with cream'.format(e.name, e.kind, e.taste, listaAll, e.filling))