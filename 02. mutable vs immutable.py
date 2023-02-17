# każda zmienna ma swój identyfikator określający miejsce w pamięci
# zmiana wartości w zmiennej powoduje nadanie nowego identyfikatora (nowego miejsca)
# powyższe oznacza że zmienna jest niezmienna (immutable) bo każda zmiana zapisuje się w noym miejscu pamięci

# istnieją zmienne które nie są zmienne (mutable)
# taką zmienną jest np lista, której wartości są zapisywane w tym samym miejscu pamięci

days = ['mon','tue','wed','thu','fri','sat','sun']
workdays = days.copy()

days.pop(5)
days.pop(5)

print(days, workdays)
