
farmacia = open("farmacie.CSV", "r", encoding = "ISO-8859-1")

# campi = []
index = 0
campi = (farmacia.readline().split(";"))
for campo in campi:
    print(f'{index} - {campo}')
    index += 1
print("="*40)
elementi = []
farmacie_effettive = []
tipologia = {}
numero_farmacie = 0
index = 0
quella_precedente = ""
for farm in farmacia.readlines():
    provvisoria = elementi.append(farm.split(";"))
    if elementi[index][2] != quella_precedente:
        quella_precedente = elementi[index][2]
        numero_farmacie += 1

        if len(tipologia) != 0:
            trovato = False
            for x in tipologia.items():
                if x[0].upper() == elementi[index][16].upper():
                    tipologia[f"{x[0].upper()}"] += 1
                    trovato = True
                    break
            if trovato == False:
                tipologia[elementi[index][16].upper()] = 1
        else:
            tipologia[elementi[index][16].upper()] = 1


        # print(f"Elemento numero {elementi[index][0]}\n"
        #       f"Denominazione: {elementi[index][3]}\n"
        #       f"Via: {elementi[index][2]}\n"
        #       f"Comune: {elementi[index][7]} ({elementi[index][10]})\n" +
        #       f"Coordinate: https://www.google.com/maps/search/?api=1&query={str(elementi[index][18]).replace(',', '.')},{str(elementi[index][19]).replace(',','.')}")
    index += 1
    farmacie_effettive.append(provvisoria)

print(f"Totale Farmacie inserite: {numero_farmacie}")
print(f"Tipologie:\n")
for tipo in tipologia.items():
    print(f"{tipo[0]} - {tipo[1]}")
farmacia.close()