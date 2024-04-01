import sqlite3
import json

def create_studenti_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS studenti (
                        id INTEGER PRIMARY KEY,
                        alunno TEXT,
                        religione INTEGER,
                        lingua_lettura INTEGER,
                        lingua_inglese INTEGER,
                        storia INTEGER,
                        educazione_civica INTEGER,
                        matematica INTEGER,
                        diritto_economia INTEGER,
                        fisica INTEGER,
                        chimica INTEGER,
                        tecn_informatiche INTEGER,
                        tecn_di_rappresentazione INTEGER,
                        sc_terra_geo INTEGER,
                        scienze_mot_sport INTEGER,
                        comportamento INTEGER,
                        media FLOAT,
                        esito TEXT
                    )''')
    conn.commit()

def populate_studenti_table(conn, data):
    cursor = conn.cursor()
    for record in data:
        cursor.execute('''INSERT INTO studenti (
                            alunno, religione, lingua_lettura, lingua_inglese, storia,
                            educazione_civica, matematica, diritto_economia, fisica, chimica,
                            tecn_informatiche, tecn_di_rappresentazione, sc_terra_geo, scienze_mot_sport,
                            comportamento, media, esito
                          ) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                          (record['Alunno'], record['RELIGIONE'], record['LINGUA E LETT.IT'], 
                           record['LINGUA INGLESE'], record['STORIA'], record['EDUCAZIONE CIVICA'],
                           record['MATEMATICA'], record['DIRITTO ED ECONOMIA'], record['FISICA'],
                           record['CHIMICA'], record['Tecn.informatiche'], record['Tecn.e Tecn.di rappr'],
                           record['SC.DELLA TERRA/GEO'], record['SCIENZE MOT. E SPORT'], record['COMPORTAMENTO'],
                           record['Media'], record['Esito']))
    conn.commit()
def get_studenti_con_debito(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT alunno, religione, lingua_lettura, lingua_inglese, storia,
                            educazione_civica, matematica, diritto_economia, fisica, chimica,
                            tecn_informatiche, tecn_di_rappresentazione, sc_terra_geo, scienze_mot_sport,
                            comportamento, media, esito
                     FROM studenti 
                     WHERE Esito = 'Sospensione del giudizio' ''')

    rows = cursor.fetchall()
    return rows

def main():
    # Leggi i dati dal file JSON
    with open('studentiFinale.json', 'r') as json_file:
        json_data = json.load(json_file)
    
    # Creazione del database SQLite3 e della tabella
    conn = sqlite3.connect('studenti.db')
    create_studenti_table(conn)
    
    # Popolamento della tabella con i dati dal file JSON
    populate_studenti_table(conn, json_data)
    
    # Esempio di interrogazione SQL per ottenere studenti con comportamento insufficiente
    studenti_con_debito = get_studenti_con_debito(conn)
    print("Studenti con il debito:")
    for studente in studenti_con_debito:
        # Modifica il primo valore della tupla
        studente_lista = list(studente)
        studente_lista[0] = str(studente_lista[0])
        studente_modificato = tuple(studente_lista)
        print(studente_modificato)
    
    # Chiusura della connessione al database
    conn.close()

if __name__ == "__main__":
    main()
