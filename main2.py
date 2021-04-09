
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
index = 0
quella_precedente = ""
for farm in farmacia.readlines():
    provvisoria = farm.split(";")
    if provvisoria[2].upper() != quella_precedente:
        farmacie_effettive.append(provvisoria)
        quella_precedente = provvisoria[2].upper()

    if len(tipologia) == 0:
       tipologia[provvisoria[16].upper()] = 1
    else:
        elemento_tipologia = [item for item in tipologia.items() if item[0].upper() == provvisoria[16].upper()]
        if len(elemento_tipologia) == 0:
            tipologia[provvisoria[16].upper()] = 1
        else:
            tipologia[f"{provvisoria[16].upper()}"] += 1

print(f"Farmacie Effettive: {len(farmacie_effettive)}\n")
[(print(x + " - " + str(tipologia[x]))) for x in tipologia.keys()]


farmacia.close()