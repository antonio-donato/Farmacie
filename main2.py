from datetime import datetime

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


datetime.strptime("01/01/2021", "%d/%m/%Y")

#  inizializzo la list vuota con numero di campi max in modo da non dover testare il primo elemento
quella_precedente = []
for x in range((len(campi) + 1)):
    quella_precedente.append("")

conta = 0
for farm in farmacia.readlines():
    provvisoria = farm.split(";")

    #  Correggo alcuni errori nel file .csv
    if provvisoria[16].upper() == "ORDINARA":
        provvisoria[16] = "Ordinaria"
    if provvisoria[16].upper() in {"-", "01/04/2021", "LOMBARDIA"}:
        provvisoria[16] = "*****"

    # Mantengo soltanto le farmacie che hanno
    if quella_precedente[2].upper() != provvisoria[2]:
        if len(farmacie_effettive) == 0:
            conta += 1
            farmacie_effettive.append(provvisoria)
        else:
            try:
                d1 = datetime.strptime(quella_precedente[14], "%d/%m/%Y")
                d2 = datetime.strptime(provvisoria[14], "%d/%m/%Y")
                if d2 > d1:
                    conta += 1
                    farmacie_effettive.append(provvisoria)
                    # print("{0:>5} ".format(conta) + f"Date: {d2} - {d1}")
            except:
                pass
        quella_precedente = provvisoria

farmacia.close()

for farm in farmacie_effettive:
    if len(tipologia) == 0:
       tipologia[farm[16].upper()] = 1
    else:
        elemento_tipologia = [item for item in tipologia.items() if item[0].upper() == farm[16].upper()]
        if len(elemento_tipologia) == 0:
            tipologia[farm[16].upper()] = 1
        else:
            tipologia[f"{farm[16].upper()}"] += 1

print(f"Farmacie Effettive: {len(farmacie_effettive)}\n" + "="*40 + "\n")

#  Titolo centrato
print("{0:^40}".format("Tabella Tipologie"))
print("-"*40)

#  allineamento della stringa chiave a destra
# [(print("{0:>30}".format(x) + " - " + str(tipologia[x]))) for x in tipologia.keys()]

#  Centratura di Tipologia e conteggio
[(print("{0:^40}".format(f"{x} - {tipologia[x]}"))) for x in tipologia.keys()]

