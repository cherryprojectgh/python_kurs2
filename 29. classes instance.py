#klasa
class Car:

    numberOfCars = 0
    listOfCars = []

    #obiekt
    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK):
        #atrybuty
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
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
        print('------------------------')

print('Class level veriables BEFORE creating instances:', Car.numberOfCars, Car.listOfCars)

#instancja klasy
car01 = Car('Seat', 'Ibiza', True, True, True)
car02 = Car('Opel', 'Corsa', True, False, True)

print('Class level veriables AFTER creating instances:', Car.numberOfCars, Car.listOfCars)

print(car01.brand, car01.is_damaged())
print(car02.brand, car02.is_damaged())

car01.get_info()
car02.get_info()

#można sprawdzić do której klasy należy wskazana instancja
print('Check if object belongs to class', isinstance(car01,Car))
print('Check if object belongs to class using type:', type(car01) is Car)
print('Check class of an object using __class__:', car01.__class__)

#sprawdzanie jakie atrybuty posiada instancja
print('List of instance attributes with values',vars(car01))
print('List of instance attributes with values',vars(Car))

print('List of instance attributes with values:', dir(car01))
print('List of class attributes with values:',    dir(Car))

print('Value taken from instnace', car01.numberOfCars, 'Value taken from class', Car.numberOfCars)

#--------------------------------------------------------------------------------------------

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind if kind in Cake.known_types else 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        Cake.bakery_offer.append(self)


    def show_info(self):
        print('-'*30)
        print('Nazwa produktu:      {}'.format(self.name.upper()))
        print('Rodzaj ciasta        {}'.format(self.kind))
        print('Smak:                {}'.format(self.taste))
        print('Dodatki:             {}'.format('Brak' if not self.additives else self.additives))
        print('Nadzienie            {}'.format('Brak' if not self.filling else self.filling ))

    def set_filling(self, filling):
        self.filling = filling

    def add_addictives(self, additives):
        self.additives.extend(additives)

cake01 = Cake('trufla','ciastko','słodki', ['element1', 'element2'], '')
cake02 = Cake('coś tam','tort','gorzki', [], 'czekoladowy')


for e in Cake.bakery_offer:
    e.show_info()


cake01.show_info()
#cake02.show_info()

cake01.set_filling('dupa')
cake01.add_addictives(['blabla1', 'blabla2'])
cake01.show_info()

print(isinstance(cake01,Cake))