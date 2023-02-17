print()

options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

def display_options():
    n = 0
    for option in options:
        n+=1
        print(n, option)

def choice_option(choice):
    choice = int(choice)

    if choice >= 0 and choice < 4:
        return options[choice-1]
    else:
        return 'Wybierz opcję w zakresie 1-3'
        
display_options()

while choice:
    choice = input('Select option above or press enter to exit: ')
    if choice:
        print(choice_option(choice))