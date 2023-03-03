brandOnSale = 'Opel'

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

    def __get_in_on_sale(self):
        return self.__isOnSale
    
    def __set_is_on_sale (self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status isOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status isOnSale. Sale valid only for {}'.format(brandOnSale))

    #właściwości klasy
    isOnSale = property(__get_in_on_sale, __set_is_on_sale, None, 'if set to true, the car is available in salke/promo')

    # Dekorator klasy method
    # cls - skrót od class
    # * - poowduje, że split nie zwraca listy tylko wartości. Do metody __init__ zostana przekazane wartości a nie lista
    @classmethod 
    def read_from_text(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar
    
    @staticmethod
    def convert_km_kw(km):
        return km * 0.735
    
    @staticmethod
    def convert_kw_km(kw):
        return kw * 1.36

lineOfText = 'Renault:Megane:True:True:False:False'
car03 = Car.read_from_text(lineOfText)

#instancja klasy
car01 = Car('Seat', 'Ibiza', True, True, True, False)
car02 = Car('Opel', 'Corsa', True, False, True, False)

car01.get_info()
car02.get_info()
car03.get_info()

print('converting 120KM to KW', Car.convert_km_kw(120))
print('converting 90KW to KM', Car.convert_km_kw(90))

print('-'*50)
#----------------------------------------------------------------------------------------------------------------------------

import pickle

class Cake:

    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, glutenFree, text):
        self.name = name
        self.kind = kind if kind in Cake.known_types else 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__glutenFree = glutenFree
        self.__text = text if kind == 'cake' or text == '' else print('coś poszło nie tak') 
        Cake.bakery_offer.append(self)

    def show_info(self):
        print('-'*30)
        print('Nazwa produktu:   {}'.format(self.name.upper()))
        print('Rodzaj ciasta     {}'.format(self.kind))
        print('Smak:             {}'.format(self.taste))
        print('Dodatki:          {}'.format('Brak' if not self.additives else self.additives))
        print('Nadzienie         {}'.format('Brak' if not self.filling else self.filling ))
        print('Gluten            {}'.format(self.__glutenFree))
        print('Tekst             {}'.format(self.__text))

    def set_filling(self, filling):
        self.filling = filling

    def add_addictives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text
    
    def __set_text(self, newText):
        if self.kind == 'cake':
            self.__text = newText
        else:
            print('coś znowu poszło nie tak')

    #właściwości funkcji
    Text = property(__get_text, __set_text, None, 'lipa panie, lipa')

    def save_to_file(self, path):
        with open(path,'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path,'rb') as file:
            newCake = pickle.load(file)

            cls.bakery_offer.append(newCake)
            return newCake



cake01 = Cake('trufla','cake','słodki', ['element1', 'element2'], '',True,'')
cake02 = Cake('coś tam','tort','gorzki', [], 'czekoladowy',False,'')



file_path = r'D:\PROJEKTY\Python\PLIKI'

# cake01.save_to_file('\\'.join([file_path, Cake.__name__ + '01.bakery']))
# cake02.save_to_file('\\'.join([file_path, Cake.__name__ + '02.bakery']))


Cake03 =  Cake.read_from_file(file_path + '\\Cake01.bakery')

for e in Cake.bakery_offer:
    e.show_info()