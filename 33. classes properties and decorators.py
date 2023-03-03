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
    
    @property
    def is_on_sale(self):
        return self.__isOnSale
    
    @is_on_sale.setter
    def is_on_sale (self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status isOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status isOnSale. Sale valid only for {}'.format(brandOnSale))

    @is_on_sale.deleter
    def is_on_sale(self):
        self.__isOnSale = None

    @property
    def car_title(self):
        return 'Brand: {}, Model: {}'.format(self.brand, self.model).title()

car01 = Car('Seat', 'Ibiza', True, True, True, False)
car02 = Car('Opel', 'Corsa', True, False, True, False)

print('-'*50)
print(car01.is_on_sale)
car01.is_on_sale = True
print(car01.is_on_sale)
print(car01.car_title)

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

    @property
    def Text(self):
        return self.__text
    
    @Text.setter
    def Text(self, newText):
        if self.kind == 'cake':
            self.__text = newText
        else:
            print('coś znowu poszło nie tak')

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

cake01.Text = 'Dupa'
print(cake01.Text)
