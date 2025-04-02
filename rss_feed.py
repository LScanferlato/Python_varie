import xml.etree.ElementTree as ET
from datetime import datetime

# Funzione per creare un elemento XML con tag e attributi specificati
def crea_elemento(tag, attributi=None, testo=None):
    elem = ET.Element(tag)
    if attributi is not None:
        for nome, valore in attributi.items():
            elem.set(nome, valore)
    if testo is not None:
        elem.text = testo
    return elem

# Funzione ausiliaria per creare elementi con testo
def crea_elemento_con_testo(tag, testo, padre):
    elem = ET.SubElement(padre, tag)
    elem.text = testo

# Dati da inserire nel feed RSS
dati_feed = {
    "titolo": "Il mio Feed RSS",
    "link": "https://example.com",
    "descrizione": "Descrizione del mio feed RSS"
}

# Lista degli articoli da includere nel feed
articoli = [
    {"titolo": "Articolo 1", "link": "https://example.com/articolo1", "pubblicazione": datetime(2023, 9, 1), "descrizione": "Descrizione dell'articolo 1"},
    {"titolo": "Articolo 2", "link": "https://example.com/articolo2", "pubblicazione": datetime(2023, 9, 15), "descrizione": "Descrizione dell'articolo 2"}
]

# Creazione del documento XML (RSS)
root = ET.Element("rss")
root.set("version", "2.0")

channel = crea_elemento("channel")
root.append(channel)

# Informazioni sul canale
crea_elemento_con_testo("title", dati_feed["titolo"], channel)
crea_elemento_con_testo("link", dati_feed["link"], channel)
crea_elemento_con_testo("description", dati_feed["descrizione"], channel)

# Aggiunta degli articoli al canale
for articolo in articoli:
    item = crea_elemento("item")
    channel.append(item)
    
    # Dettagli dell'articolo
    crea_elemento_con_testo("title", articolo["titolo"], item)
    crea_elemento_con_testo("link", articolo["link"], item)
    crea_elemento_con_testo("pubDate", articolo["pubblicazione"].strftime("%a, %d %b %Y %H:%M:%S +0000"), item)  # Formattazione data secondo lo standard RSS
    crea_elemento_con_testo("description", articolo["descrizione"], item)

# Scrittura del file RSS
tree = ET.ElementTree(root)
with open('output.rss', 'wb') as f:
    tree.write(f, encoding='utf-8', xml_declaration=True)

print("File RSS generato correttamente.")
