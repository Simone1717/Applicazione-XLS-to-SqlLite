import json

# Leggi il file JSON
with open('studenti.json', 'r') as f:
    data = json.load(f)

# Rinomina le chiavi degli oggetti
for item in data:
    item["Pr"] = item.pop("Unnamed: 0")
    item["Alunno"] = item.pop("Unnamed: 1")
    item["RELIGIONE"] = item.pop("Unnamed: 10")
    item["LINGUA E LETT.IT"] = item.pop("Unnamed: 11")
    item["LINGUA INGLESE"] = item.pop("Unnamed: 12")
    item["STORIA"] = item.pop("Unnamed: 13")
    item["EDUCAZIONE CIVICA"] = item.pop("Unnamed: 14")
    item["MATEMATICA"] = item.pop("Unnamed: 15")
    item["DIRITTO ED ECONOMIA"] = item.pop("Unnamed: 16")
    item["FISICA"] = item.pop("Unnamed: 17")
    item["CHIMICA"] = item.pop("Unnamed: 18")
    item["Tecn.informatiche"] = item.pop("Unnamed: 19")
    item["Tecn.e Tecn.di rappr"] = item.pop("Unnamed: 20")
    item["SC.DELLA TERRA/GEO"] = item.pop("Unnamed: 21")
    item["SCIENZE MOT. E SPORT"] = item.pop("Unnamed: 22")
    item["COMPORTAMENTO"] = item.pop("Unnamed: 23")
    item["Media"] = item.pop("Unnamed: 24")
    item["Esito"] = item.pop("Unnamed: 27")

    # Rimuovi le colonne vuote aggiuntive
    del item["Unnamed: 2"]
    del item["Unnamed: 3"]
    del item["Unnamed: 4"]
    del item["Unnamed: 5"]
    del item["Unnamed: 6"]
    del item["Unnamed: 7"]
    del item["Unnamed: 8"]
    del item["Unnamed: 9"]
    del item["Unnamed: 25"]
    del item["Unnamed: 26"]

# Salva il file JSON con le chiavi rinominate
with open('studentiFinale.json', 'w') as f:
    json.dump(data, f, indent=4)