import csv
import types

def export_to_file_static(path, header, data):
    with open(path, mode='w') as file:
        #obiekt wiritter stworzony w oparciu o moduł CSV. Ten obiekt definuje jak pracować z plikiem CSV 
        # delimiter - określa jakim znakiem będą porozdzielane wartości, np. przecinkiem
        # quotechar - jeżeli treść zawiera przecinki to wartość będzie zamknięta np. cudzysłowiem
        # quoting   - jak mocno mająbyć cytowe wartości, minimal oznacza cytat tylko jeżeli w tekście był gdzieśww. zdefiniowany przecinek
        writter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writter.writerow(header)
        writter.writerow(data)
    print('This is function expoert_to_file - static method')

def export_to_file_class(cls, path):
    with open(path, mode='w') as file:
        writter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writter.writerow(['brand', 'model', 'IsOnSale'])
        for element in cls.listOfCars:
            writter.writerow([element.brand, element.model, element.is_on_sale])
    print('This is function expoert_to_file - class method')

def export_to_file_instance(self, path):
    with open(path, mode='w') as file:
        writter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writter.writerow(['brand', 'model', 'IsOnSale'])
        for element in self.listOfCars:
            writter.writerow([element.brand, element.model, element.is_on_sale])
    print('This is function expoert_to_file - instance method')


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

filePath_s = r'D:\PROJEKTY\Python\PLIKI\export_static.csv'
filePath_c = r'D:\PROJEKTY\Python\PLIKI\export_class.csv'
filePath_i = r'D:\PROJEKTY\Python\PLIKI\export_instance.csv'

print('Static---------'*5)
export_to_file_static(filePath_s, ['Brand','Model','isOnSale'], [car01.brand, car01.model, car01.is_on_sale])

# odwołujemy się do definicji klasy - tworze funkcję do której przypisuje zewnętrzną funkcję
# Car.export_to_file_STATIC = export_to_file_static

print('Class---------'*5)
# trzeba zaimportować moduł types aby połączyć zewnętrzną funkcję z klasą
Car.export_to_file_CLASS = types.MethodType(export_to_file_class, Car)
Car.export_to_file_CLASS(filePath_c)

print('Instance---------'*5)
car01.export_to_file_INSTANCE = types.MethodType(export_to_file_instance, car01)
car01.export_to_file_INSTANCE(filePath_i)

#---------------------------------------------------------------------------------------

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

def export_1_cake_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as file:
        content = template.format(cls.name, cls.kind, cls.taste, cls.additives, cls.filling)
        file.write(content)

#filePath_s = r'D:\PROJEKTY\Python\PLIKI\export_static.csv'
print('*'*60,'STATIC')
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, r'D:\PROJEKTY\Python\PLIKI\s_cake.html')

def export_all_cake_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as file:
        for element in cls.bakery_offer:
            content = template.format(element.name, element.kind, element.taste, element.additives, element.filling)
            file.write(content)

#filePath_s = r'D:\PROJEKTY\Python\PLIKI\export_static.csv'
print('*'*60,'CLASS')
Cake.export_all_cake_to_html = types.MethodType(export_all_cake_to_html, Cake)
Cake.export_all_cake_to_html(r'D:\PROJEKTY\Python\PLIKI\c_cake.html')

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""
 
    with open(path, "w") as file:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        file.write(content)

print('*'*60,'INSTANCE')

for element in Cake.bakery_offer:
    Cake.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, element)

for element in Cake.bakery_offer:
    element.export_this_cake_to_html('D:\\PROJEKTY\\Python\\PLIKI\\{}.html'.format(element.name))

for element in Cake.bakery_offer:
    element.show_info()

