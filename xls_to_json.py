import pandas as pd
import json

def excel_to_json(excel_file):
    try:
        df = pd.read_excel(excel_file)
    except FileNotFoundError:
        print("File non trovato.")
        return None
    except Exception as e:
        print("Si è verificato un errore durante la lettura del file Excel:", str(e))
        return None
    
    # Assegna manualmente i nomi delle colonne
    column_names = ["Pr.", "Alunno", "RELIGIONE", "LINGUA E LETT.IT", "LINGUA INGLESE", "STORIA", "EDUCAZIONE CIVICA", "MATEMATICA", "DIRITTO ED ECONOMIA", "FISICA", "CHIMICA", "Tecn.informatiche", "Tecn.e Tecn.di rappr", "SC.DELLA TERRA/GEO", "SCIENZE MOT. E SPORT", "COMPORTAMENTO", "Media", "Esito"]
    df.columns = column_names
    
    # Trasforma il DataFrame in un dizionario
    data_dict = df.to_dict(orient='records')
    
    # Aggiungi il codice sopra per convertire i dati in un DataFrame di pandas e gestire correttamente i dati NaN
    data_types = [str if pd.isna(data_type) else data_type for data_type in data_dict[1].values()]
    data_rows = [row for row in data_dict[2:]]
    df = pd.DataFrame(data_rows, columns=column_names)
    for column, data_type in zip(df.columns, data_types):
        if pd.isna(data_type):
            df[column] = df[column].astype(str)
        else:
            df[column] = df[column].astype(data_type)
    
    return df

def main():
    excel_file = '1Sin.xlsx'  # Inserisci il nome del file Excel
    json_data = excel_to_json(excel_file)
    
    if json_data is not None:
        # Salva i dati in un file JSON
        with open('studenti.json', 'w') as json_file:
            json_file.write(json.dumps(json_data.to_dict(orient='records'), indent=4))
        print("Dati trasformati con successo in formato JSON.")
    else:
        print("Errore durante la trasformazione dei dati in formato JSON.")
