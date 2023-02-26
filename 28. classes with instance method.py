#klasa
class Car:

    #obiekt
    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK):
        #atrybuty
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
    
    #metody
    def is_damaged(self):
        return not (self.isAirbagOK and self.isPaintingOK and self.isMechanicOK)
    
    def get_info(self):
        print('{}  {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirbagOK))
        print('Painting - ok -      {}'.format(self.isPaintingOK))
        print('Mechanic - ok -      {}'.format(self.isMechanicOK))
        print('------------------------')

#instancja klasy
car01 = Car('Seat', 'Ibiza', True, True, True)
car02 = Car('Opel', 'Corsa', True, False, True)

print(car01.brand, car01.is_damaged())
print(car02.brand, car02.is_damaged())

car01.get_info()
car02.get_info()
#print(car01.brand, car01.model, car01.isAirbagOK, car01.isPaintingOK, car01.isMechanicOK)
#print(car02.brand, car02.model, car02.isAirbagOK, car02.isPaintingOK, car02.isMechanicOK)

#--------------------------------------------------------------------------------------------

class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind 
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print('-'*30)
        print('Nazwa produktu:      {}'.format(self.name.upper()))
        print('Smak:                {}'.format(self.taste))
        print('Dodatki:             {}'.format('Brak' if not self.additives else self.additives))
        print('Nadzienie            {}'.format('Brak' if not self.filling else self.filling ))

    def set_filling(self, filling):
        self.filling = filling

    def add_addictives(self, additives):
        self.additives.extend(additives)



lista = ['element1', 'element2']
listaAll = ' '.join(lista)

cake01 = Cake('trufla','ciastko','słodki', lista, '')
cake02 = Cake('coś tam','tort','gorzki', [], 'czekoladowy')

print(cake01.name)

bakery_offer = [cake01, cake02]

for e in bakery_offer:
    print('{} - {} main taste: {} with additives of {}, filled with cream'.format(e.name, e.kind, e.taste, listaAll, e.filling))

cake01.show_info()
#cake02.show_info()

cake01.set_filling('dupa')
cake01.add_addictives(['blabla1', 'blabla2'])
cake01.show_info()