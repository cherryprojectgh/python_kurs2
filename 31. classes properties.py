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


#instancja klasy
car01 = Car('Seat', 'Ibiza', True, True, True, False)
car02 = Car('Opel', 'Corsa', True, False, True, False)

car01.get_info()
car02.get_info()

car01.isOnSale = True
car02.isOnSale = True

car01.get_info()
car02.get_info()

#--------------------------------------------------------------------------------------------

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

cake01 = Cake('trufla','cake','słodki', ['element1', 'element2'], '',True,'')
cake02 = Cake('coś tam','tort','gorzki', [], 'czekoladowy',False,'')

cake01.Text = 'duuuuppaaaaaa'
cake02.Text = 'duuuuppaaaaaa'

for e in Cake.bakery_offer:
    e.show_info()
