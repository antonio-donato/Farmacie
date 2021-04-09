
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

    #  Correggo alcuni errori nel file .csv
    if provvisoria[16].upper() == "ORDINARA":
        provvisoria[16] = "Ordinaria"
    if provvisoria[16].upper() in {"-", "01/04/2021", "LOMBARDIA"}:
        provvisoria[16] = "*****"

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

print(f"Farmacie Effettive: {len(farmacie_effettive)}\n" + "="*40 + "\n")

#  Titolo centrato
print("{0:^40}".format("Tabella Tipologie"))
print("-"*40)

#  allineamento della stringa chiave a destra
# [(print("{0:>30}".format(x) + " - " + str(tipologia[x]))) for x in tipologia.keys()]

#  Centratura di Tipologia e conteggio
[(print("{0:^40}".format(f"{x} - {tipologia[x]}"))) for x in tipologia.keys()]

farmacia.close()