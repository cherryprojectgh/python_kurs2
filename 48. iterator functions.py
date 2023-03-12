import csv
 
with open(r"D:\PROJEKTY\Python\PLIKI\dupa.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#    for row in csvreader:
#        print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration as error:
            break
