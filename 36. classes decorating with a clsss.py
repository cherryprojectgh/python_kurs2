import random

class MemoryClass:
    list_of_already_selected_items = []

    def __init__(self, function):
        print('>> this is init of MemoryClass')
        self.function = function

    def __call__(self, list):
        print('>> This is call of MemoryClass instance')
        items_not_selected = [element for element in list if element not in MemoryClass.list_of_already_selected_items]
        print('>> Selecting only from a list of', items_not_selected)
        item = self.function(items_not_selected)
        MemoryClass.list_of_already_selected_items.append(item)
        return item

cars = ['Opel','Toyota','Fiat','Ford','Renault','Mercedes','BMW','Peugeot','Porsche','Audi','VW','Mazda']

@MemoryClass
def select_today_promotion(listOfCars):
    return random.choice(listOfCars)

@MemoryClass
def select_today_show(listOfCars):
    return random.choice(listOfCars)

@MemoryClass
def select_free_accessories(listOfCars):
    return random.choice(listOfCars)

print('-'*60)
print('Promotion:', select_today_promotion(cars))
print('Show:', select_today_show(cars))
print('Free accesories:', select_free_accessories(cars))

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
 
    def add_additives(self, additives):
        self.additives.extend(additives)


class NoDuplicates:

    listOfSelectedItems = []

    def __init__(self, function):
        self.function = function

    def __call__(self, cake, listOfadditives):
        print('>>Sprawdzam czy jest możliwe dobranie dodatku do wypieku')
        for element in listOfadditives:
            if element not in cake.additives:
                cake.additives.append(element)


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

print('-'*60)
cake01.show_info()

@ NoDuplicates
def add_extra_additives(listOfAdditives):
    return cake01.show_info()

@ NoDuplicates
def add_extra_additives(listOfAdditives):
    return cake01.show_info()


add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()

add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolate', 'nuts'])
cake01.show_info()