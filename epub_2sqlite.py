import os
import sqlite3
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Funzione per estrarre testo e metadati da un file EPUB
def extract_text_and_metadata_from_epub(file_path):
    book = epub.read_epub(file_path)
    text = ""
    for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = BeautifulSoup(doc.content, 'html.parser')
        text += soup.get_text()
    
    # Estrazione dei metadati
    title = book.get_metadata('DC', 'title')[0][0] if book.get_metadata('DC', 'title') else 'Unknown'
    author = book.get_metadata('DC', 'creator')[0][0] if book.get_metadata('DC', 'creator') else 'Unknown'
    subject = book.get_metadata('DC', 'subject')[0][0] if book.get_metadata('DC', 'subject') else 'Unknown'
    
    return title, author, subject, text

# Creazione del database SQLite
def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ebooks
                      (id INTEGER PRIMARY KEY, title TEXT, author TEXT, subject TEXT, content TEXT)''')
    conn.commit()
    return conn

# Inserimento del testo e metadati nel database
def insert_text_and_metadata_into_db(conn, title, author, subject, content):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ebooks (title, author, subject, content) VALUES (?, ?, ?, ?)", (title, author, subject, content))
    conn.commit()

# Percorso della cartella contenente gli eBook
folder_path = '/home/lxuser/OneDrive/EBooks"
db_name = 'ebooks.db'

# Creazione del database
conn = create_database(db_name)

# Iterazione sui file nella cartella
for file_name in os.listdir(folder_path):
    if file_name.endswith('.epub'):
        file_path = os.path.join(folder_path, file_name)
        title, author, subject, text = extract_text_and_metadata_from_epub(file_path)
        insert_text_and_metadata_into_db(conn, title, author, subject, text)

# Chiusura della connessione al database
conn.close()
