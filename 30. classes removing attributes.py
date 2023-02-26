#klasa
class Car:

    numberOfCars = 0
    listOfCars = []

    #obiekt
    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK, isOnSale):
        #atrybuty
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale #wewnętrzne, schowane
        Car.numberOfCars += 1
        Car.listOfCars.append(self)
    
    #metody
    def is_damaged(self):
        return not (self.isAirbagOK and self.isPaintingOK and self.isMechanicOK)
    
    def get_info(self):
        print('{}  {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirbagOK))
        print('Painting - ok -      {}'.format(self.isPaintingOK))
        print('Mechanic - ok -      {}'.format(self.isMechanicOK))
        print('IS ON SALE           {}'.format(self.__isOnSale))
        print('------------------------')

#instancja klasy
car01 = Car('Seat', 'Ibiza', True, True, True, False)
car02 = Car('Opel', 'Corsa', True, False, True, True)

#klasy można modyfikować w trakcie życia obiektu

car01.YearOfProduction = 2005 #dodawania atrybutu
del car01.YearOfProduction #usuwanie atrybutu

#Są dedykowane metody do modyfikacji atrybutów
setattr(car01, 'TAXI', False)
delattr(car01,'TAXI')
print('Czy atrybut istnieje: ',hasattr(car01, 'TAXI'),'\n') #sprawdzanie czy atrybut istnieje

car01.get_info()
print(vars(car01))

#--------------------------------------------------------------------------------------------

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, __glutenFree):
        self.name = name
        self.kind = kind if kind in Cake.known_types else 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.glutenFree = __glutenFree
        Cake.bakery_offer.append(self)


    def show_info(self):
        print('-'*30)
        print('Nazwa produktu:      {}'.format(self.name.upper()))
        print('Rodzaj ciasta        {}'.format(self.kind))
        print('Smak:                {}'.format(self.taste))
        print('Dodatki:             {}'.format('Brak' if not self.additives else self.additives))
        print('Nadzienie            {}'.format('Brak' if not self.filling else self.filling ))
        print('Gluten               {}'.format(self.__glutenFree))

    def set_filling(self, filling):
        self.filling = filling

    def add_addictives(self, additives):
        self.additives.extend(additives)

cake01 = Cake('trufla','ciastko','słodki', ['element1', 'element2'], '',True)
cake02 = Cake('coś tam','tort','gorzki', [], 'czekoladowy',False)


for e in Cake.bakery_offer:
    e.show_info()






"""
cake01.show_info()
#cake02.show_info()

cake01.set_filling('dupa')
cake01.add_addictives(['blabla1', 'blabla2'])
cake01.show_info()

print(isinstance(cake01,Cake))
print(type(car01) is Car)

print(vars(car01))
print(vars(Car))

print(dir(car01))
print(dir(Car))
"""
