
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
quella_precedente = ""
for farm in farmacia.readlines()[:1000]:
    elementi.append(farm.split(";"))
    if elementi[index][2] != quella_precedente:
        quella_precedente = elementi[index][2]
        print(f"Elemento numero {elementi[index][0]}\n"
              f"Denominazione: {elementi[index][3]}\n"
              f"Via: {elementi[index][2]}\n"
              f"Comune: {elementi[index][7]} ({elementi[index][10]})\n" +
              f"Coordinate: https://www.google.com/maps/search/?api=1&query={str(elementi[index][18]).replace(',', '.')},{str(elementi[index][19]).replace(',','.')}")
    index += 1

farmacia.close()