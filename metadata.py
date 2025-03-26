import os
from PyPDF2 import PdfReader

# Specifica la cartella che contiene i file PDF
cartella_ebook = "/home/lxuser/OneDrive/EBooks/PDF/AI"

# Crea una lista per memorizzare i metadata
metadata = []

# Funzione per iterare su tutte le sottocartelle
def iterare_sottocartelle(cartella):
    for filename in os.listdir(cartella):
        file_path = os.path.join(cartella, filename)
        if os.path.isfile(file_path):
            # Verifica se il file è un PDF
            if filename.endswith(".pdf"):
                print(f"Processing file: {file_path}")
                # Apri il file PDF
                pdf_file = open(file_path, "rb")
                pdf_reader = PdfReader(pdf_file)
                
                # Estrae i metadata
                info = pdf_reader.metadata
                title = getattr(info, 'title', None)
                author = getattr(info, 'author', None)
                creator = getattr(info, 'creator', None)
                producer = getattr(info, 'producer', None)
                subject = getattr(info, 'subject', None)
                keywords = getattr(info, 'keywords', None)
                
                # Aggiungi i metadata alla lista
                metadata.append({
                    "filename": filename,
                    "path": file_path,
                    "title": title,
                    "author": author,
                    "creator": creator,
                    "producer": producer,
                    "subject": subject,
                    "keywords": keywords
                })
                
                # Chiudi il file PDF
                pdf_file.close()
        elif os.path.isdir(file_path):
            # Se è una sottocartella, chiama la funzione ricorsivamente
            iterare_sottocartelle(file_path)

# Chiama la funzione per iterare su tutte le sottocartelle
iterare_sottocartelle(cartella_ebook)

# Salva i metadata in un file di testo
with open('metadata.txt', 'w') as f:
    for libro in metadata:
        f.write(f"File: {libro['filename']}\n")
        f.write(f"Percorso: {libro['path']}\n")
        f.write(f"Titolo: {libro['title']}\n")
        f.write(f"Autore: {libro['author']}\n")
        f.write(f"Creatore: {libro['creator']}\n")
        f.write(f"Prodotto da: {libro['producer']}\n")
        f.write(f"Oggetto: {libro['subject']}\n")
        f.write(f"Parole chiave: {libro['keywords']}\n")
        f.write("-" * 50 + "\n")

print("Metadata saved to metadata.txt")
