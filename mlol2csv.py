from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
import csv
from bs4 import BeautifulSoup

# Imposta il percorso corretto di ChromeDriver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service)

# Crea una cartella per salvare gli HTML
os.makedirs("html_medialibrary", exist_ok=True)

# Numero totale di pagine da salvare
total_pages = 8
for page in range(1, total_pages + 1):
    url = f"https://www.medialibrary.it/media/ricerca.aspx?keywords=Italo+Calvino&seltip=310&page={page}"
    driver.get(url)
    time.sleep(3)  # Attendi il caricamento della pagina
    html_content = driver.page_source
    with open(f"html_medialibrary/pagina_{page}.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"✅ Salvato pagina {page}")

driver.quit()
print("✅ Completato il salvataggio di tutte le pagine.")

# Estrazione dei dati dai file HTML
libri = []

def estrai_dati_da_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        titoli = [a.get_text(strip=True) for a in soup.find_all('a') if a.get('href', '').startswith('../media/scheda.aspx')]
        autori = [a.get_text(strip=True) for a in soup.find_all('a') if a.get('href', '').startswith('ricerca.aspx?selcrea=')]
        links = [a.get('href') for a in soup.find_all('a') if a.get('href', '').startswith('../media/scheda.aspx')]

        for i in range(min(len(titoli), len(autori), len(links))):
            libri.append({
                'Titolo': titoli[i],
                'Autore': autori[i],
                'Link': f"https://www.medialibrary.it{links[i]}"
            })

# Analizza tutti i file HTML nella cartella
for filename in os.listdir("html_medialibrary"):
    if filename.endswith(".html"):
        estrai_dati_da_html(os.path.join("html_medialibrary", filename))

# Scrive i dati in un file CSV
with open("libri.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["Titolo", "Autore", "Link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for libro in libri:
        writer.writerow(libro)

print("📄 File 'libri.csv' generato con successo.")
