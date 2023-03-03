class Car:

    def __init__(self, brand, model, isAirbagOK, isPaintingOK, isMechanicOK, accesories):
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.accesories = accesories
   
    def get_info(self):
        print('')
        print('{}  {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirbagOK))
        print('Painting - ok -      {}'.format(self.isPaintingOK))
        print('Mechanic - ok -      {}'.format(self.isMechanicOK))
        print('Accesories           {}'.format(self.accesories))
        print('-'*100)
    
    def __iadd__(self, other):
        if type(other) is list:
            self.accesories.extend(other)
            return Car(self.brand, self.model, self.isAirbagOK, self.isPaintingOK, self.isMechanicOK, self.accesories)
        elif type(other) is str:
            self.accesories.append(other)
            return Car(self.brand, self.model, self.isAirbagOK, self.isPaintingOK, self.isMechanicOK, self.accesories)
        else:
            print("Błąd. Nieobsługiwany typ danych {}".format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return(self, other)
        else:
            print('Błąd. Podane dane nie są obiektem "Car"')   

    def __str__(self):
        return 'Brand {}, Model {}'.format(self.brand, self.model)



car01 = Car('Seat','Ibiza',True,True,True,['winter tires'])
car01.get_info()

car01 += ['navigation system','roof rack']
car01.get_info()

car01 += 'loudspeaker system'
car01.get_info()

car02 = Car('Opel','Corsa',True,False,True,[])

carList = car01 + car02
print(carList[0].brand, carList[1].brand)

car02 = Car('Opel','Corsa', True, False, True, [])

print(car02)

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
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    def __str__(self):
        return 'Nazwa ciasta: {}, Rodzaj ciacha: {}, Dodatki: {}'.format(self.name, self.kind, self.additives)
    
    def __iadd__(self, newAdditives):
        if type(newAdditives) is list:
            self.additives.extend(newAdditives)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)        
        elif type(newAdditives) is str:
            self.additives.append(newAdditives)
            return Cake(self.name, self.kind, self.taste, self.additives, self.filling)        
        else:
            print('Błąd. Nieobsługiwany typ danych --> {}'.format(newAdditives))
 
       
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

cake01 += 'dupa'

cake01.show_info()