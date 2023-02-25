carBrand = 'Seat'
carModel = 'Ibiza'
carIsAirbagOK = True
carIsPaintingOK = True
carIsMechanicOK = True

def is_car_damaged(carIsAirbagOK, carIsPaintingOK, carIsMechanicOK):
    return not(carIsAirbagOK and carIsPaintingOK and carIsMechanicOK)

print(is_car_damaged(carIsAirbagOK, carIsPaintingOK, carIsMechanicOK))


cake_01_taste = 'vanilia'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7
 
cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3

cake_01 =   {
            'taste':'vanilla',
            'glaze':'chocolade',
            'text':'Happy Brithday',
            'weight': 0.7
            }

cake_02 =   {
            'taste':'tee',
            'glaze':'lemon',
            'text':'Happy Python Coding',
            'weight': 1.3
            }
 
def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))
 
show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

def show_cake_info2(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(cake['taste'],cake['glaze'],cake['text'],cake['weight']))

show_cake_info2(cake_01)
show_cake_info2(cake_02)

cakes = [cake_01, cake_02]
 
for a_cake in cakes:
    show_cake_info(a_cake)