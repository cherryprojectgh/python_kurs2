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

class Truck(Car):

    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK, isOnSale, capacityKg):
        super().__init__(brand, model, isAirbagOK, isPaintingOK, isMechanicOK, isOnSale)
        self.capacityKg = capacityKg

    def get_info(self):
        super().get_info()
        print('Capacity - ok -      {}'.format(self.capacityKg))


truck01 = Truck('Ford','Transit',True,False,True,False,1600)
truck02 = Truck('Renault','Trafic',True,True,True,True,1200)

truck01.get_info()

# ----------------------------------------------------------------------------------------------------------

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print('-'*60)
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t {}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
 
    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)
    
class SuperCake(Cake):

    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text
    
    def show_info(self):
        super().show_info()
        print("Occasion:     {}".format(self.occasion))
        print("Shape:        {}".format(self.shape))
        print("Ornaments:    {}".format(self.ornaments))
        print("Text:         {}".format(self.text))

birthday = SuperCake('Fajny tort','lody','gorzki',['jakaś posypka','cukier puder'],'różane','urodziny','kwadrat','kwiatki','Wszystkiego naj')
wedding = SuperCake('Zajebisty tort','galareta','słodki',['kolorwa posypka','polewa czekoladowa'],'karmelowe','wesele','koło','serduszka','uciekaj póki możesz')

wedding.show_info()

print('*'*60)

for element in Cake.bakery_offer:
    print(element.name)
    element.show_info()