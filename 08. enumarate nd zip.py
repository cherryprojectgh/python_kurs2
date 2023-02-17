workDays = [19,21,22,21,20,22]
print(workDays)

print(workDays[2])

enumarate_days = list(enumerate(workDays))
print(enumarate_days)

for pos, value in enumarate_days:
    print('Position: ', pos, 'Value: ', value)

#-----------------------------------------------------------------------------------------

months = ['I','II','III','IV','V','VI']

months_days = list(zip(months, workDays))

print(months_days)

for m, d in months_days:
    print('Month: ', m, 'Day: ', d)

for pos, (m,d) in enumerate(zip(months, workDays)):
    print('Postion:', pos, 'Month:', m, 'Day:', d)

#-----------------------------------------------------------------------------------------

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

#wyświetl: The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...

for project, leader in zip(projects,leaders):
    print('The leader of', project, 'is', leader)



#wyświetl: The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...

for project, data, leader in zip(projects, dates, leaders):
    print('The leader of', project, 'started', data, 'is', leader)

#wyświetl: ...numer kolejny... - The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...

for index, (project, data, leader) in enumerate(zip(projects, dates, leaders)):
    print(index+1, 'The leader of', project, 'started', data, 'is', leader)
#LUB
for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))