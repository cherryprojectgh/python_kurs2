def buy_me(prefix, what='something nice'):
    print(prefix, what)

buy_me('please buy me','a new car')

#---------------------------------------------------------------

def show_progress(character, how_many):
    for _ in range(how_many):
        print(character)

show_progress('-',5)