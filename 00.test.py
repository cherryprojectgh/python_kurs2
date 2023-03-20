text = 'Programming in python.'
vowels = ['a', 'e', 'i', 'o', 'u']

text = text.lower()
text = text.replace(' ','').replace('.','')

letters = set(text)

roznica = letters.difference(vowels)
    
print('Liczba elementów:', len(roznica))

for