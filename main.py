
farmacia = open("farmacie.CSV", "r", encoding = "ISO-8859-1")

# campi = []
index = 0
campi = (farmacia.readline().split(";"))
for campo in campi:
    print(f'{index} - {campo}')
    index += 1
print("="*40)
elementi = []
index = 0
for farm in farmacia.readlines()[1:100]:
    elementi.append(farm.split(";"))
    print(f"Elemento numero {elementi[index][0]} \nDenominazione: {elementi[index][3]}\nComune: {elementi[index][7]} ({elementi[index][10]})\n" +
          f"Coordinates: https://www.google.com/maps/search/?api=1&query={str(elementi[index][18]).replace(',', '.')},{str(elementi[index][19]).replace(',','.')}")
    index += 1

farmacia.close()