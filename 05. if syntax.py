
print()

day_type = 1

weekend = 1
workday = 2
holiday = 3

if day_type == 1:
    pass
elif day_type == 2:
    pass
else:
    pass

day_description = 'weekend' if day_type == 1 else 'workday' if day_type ==2 else 'holiday'
print(day_description)

# ------------------------------------------------------------------------------------------------

price = 123
bonus = 23
bonus_granted = True
 
if bonus_granted:
    price -= bonus
 
# print(price)
# krótki zapis
print(price - bonus if bonus_granted else price)

# ------------------------------------------------------------------------------------------------

rating = 5
 
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good' if rating == 5 else 'good' if rating == 4 else 'week')