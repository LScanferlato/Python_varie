import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Lista di personaggi famosi con le loro date di nascita e morte, città natale e di morte
personaggi = [
    {"nome": "Albert Einstein", "nascita": "1879-03-14", "morte": "1955-04-18", "città_nascita": "Ulm", "città_morte": "Princeton"},
    {"nome": "Marie Curie", "nascita": "1867-11-07", "morte": "1934-07-04", "città_nascita": "Varsavia", "città_morte": "Sallanches"},
    {"nome": "Isaac Newton", "nascita": "1643-01-04", "morte": "1727-03-31", "città_nascita": "Woolsthorpe", "città_morte": "Kensington"},
    {"nome": "Leonardo da Vinci", "nascita": "1452-04-15", "morte": "1519-05-02", "città_nascita": "Vinci", "città_morte": "Amboise"},
    {"nome": "Galileo Galilei", "nascita": "1564-02-15", "morte": "1642-01-08", "città_nascita": "Pisa", "città_morte": "Arcetri"},
    {"nome": "Charles Darwin", "nascita": "1809-02-12", "morte": "1882-04-19", "città_nascita": "Shrewsbury", "città_morte": "Downe"},
    {"nome": "Nikola Tesla", "nascita": "1856-07-10", "morte": "1943-01-07", "città_nascita": "Smiljan", "città_morte": "New York"},
    {"nome": "Ada Lovelace", "nascita": "1815-12-10", "morte": "1852-11-27", "città_nascita": "Londra", "città_morte": "Londra"},
    {"nome": "Alan Turing", "nascita": "1912-06-23", "morte": "1954-06-07", "città_nascita": "Londra", "città_morte": "Wilmslow"},
    {"nome": "Stephen Hawking", "nascita": "1942-01-08", "morte": "2018-03-14", "città_nascita": "Oxford", "città_morte": "Cambridge"},
    # Imperatori romani
    {"nome": "Augusto", "nascita": "-0063-03-15", "morte": "0014-08-19", "città_nascita": "Roma", "città_morte": "Nola"},
    {"nome": "Tiberio", "nascita": "-0042-11-16", "morte": "0037-03-16", "città_nascita": "Roma", "città_morte": "Miseno"},
    {"nome": "Caligola", "nascita": "0012-08-31", "morte": "0041-01-24", "città_nascita": "Anzio", "città_morte": "Roma"},
    {"nome": "Nerone", "nascita": "0037-12-15", "morte": "0068-06-09", "città_nascita": "Anzio", "città_morte": "Roma"},
    {"nome": "Traiano", "nascita": "0053-09-18", "morte": "0117-08-08", "città_nascita": "Italica", "città_morte": "Selinus"},
    # Sovrani greci
    {"nome": "Alessandro Magno", "nascita": "-0356-07-20", "morte": "-0323-06-10", "città_nascita": "Pella", "città_morte": "Babilonia"},
    {"nome": "Pericle", "nascita": "-0495-01-01", "morte": "-0429-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Leonida I", "nascita": "-0540-01-01", "morte": "-0480-01-01", "città_nascita": "Sparta", "città_morte": "Termopili"},
    {"nome": "Filippo II di Macedonia", "nascita": "-0382-01-01", "morte": "-0336-01-01", "città_nascita": "Pella", "città_morte": "Aigai"},
    # Re e imperatori europei
    {"nome": "Carlo Magno", "nascita": "0747-04-02", "morte": "0814-01-28", "città_nascita": "Aquisgrana", "città_morte": "Aquisgrana"},
    {"nome": "Federico Barbarossa", "nascita": "1122-01-01", "morte": "1190-06-10", "città_nascita": "Haguenau", "città_morte": "Saleph"},
    {"nome": "Napoleone Bonaparte", "nascita": "1769-08-15", "morte": "1821-05-05", "città_nascita": "Ajaccio", "città_morte": "Sant'Elena"},
    {"nome": "Elisabetta I", "nascita": "1533-09-07", "morte": "1603-03-24", "città_nascita": "Greenwich", "città_morte": "Richmond"}
]

# Funzione per convertire le date in formato datetime
def converti_data(data):
    try:
        return datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        if data.startswith('-'):
            return datetime.strptime(data[1:], '%Y-%m-%d').replace(year=-int(data[1:5]))
        else:
            return datetime.strptime(data, '%Y-%m-%d')

# Creazione del DataFrame
df = pd.DataFrame(personaggi)

# Conversione delle date in formato datetime usando la funzione personalizzata
df['nascita'] = df['nascita'].apply(converti_data)
df['morte'] = df['morte'].apply(converti_data)

# Creazione del diagramma di Gantt
fig, ax = plt.subplots(figsize=(14, 10))

for i, personaggio in df.iterrows():
    ax.barh(personaggio['nome'], (personaggio['morte'] - personaggio['nascita']).days, left=personaggio['nascita'])
    ax.text(personaggio['nascita'], i, personaggio['città_nascita'], va='center', ha='right', color='blue', fontsize=8)
    ax.text(personaggio['morte'], i, personaggio['città_morte'], va='center', ha='left', color='red', fontsize=8)

# Impostazione delle etichette e del titolo
ax.set_xlabel('Anno')
ax.set_ylabel('Personaggi famosi')
ax.set_title('Diagramma di Gantt: Nascita e Morte di Personaggi Famosi')

# Formattazione delle date sull'asse x
ax.xaxis_date()

plt.show()
