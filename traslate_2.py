import os
import subprocess
from translate import Translator
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog


def convert_pdf_to_text(pdf_path):
    result = subprocess.run(['pdftotext', pdf_path, '-'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def translate_text(text, target_language='it'):
    translator = Translator(to_lang=target_language)
    translated_parts = []
    max_length = 500  # Limite massimo di caratteri per la traduzione
    total_parts = len(text) // max_length + 1
    for i in range(0, len(text), max_length):
        part = text[i:i+max_length]
        translated_part = translator.translate(part)
        translated_parts.append(translated_part)
        progress = (i // max_length + 1) / total_parts * 100
        print(f"Progresso della traduzione: {progress:.2f}%")
    return ''.join(translated_parts)

def save_translated_text(translated_text, save_path, file_format):
    if file_format == 'txt':
        with open(save_path, 'w') as f:
            f.write(translated_text)
    elif file_format == 'latex':
        with open(save_path, 'w') as f:
            f.write(f"\\documentclass{{article}}\n\\begin{{document}}\n{translated_text}\n\\end{{document}}")
    elif file_format == 'markdown':
        with open(save_path, 'w') as f:
            f.write(translated_text)

def main():
    root = tk.Tk()
    root.withdraw()  # Nascondi la finestra principale
    pdf_path = filedialog.askopenfilename(title="Seleziona il documento PDF", filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        messagebox.showerror("Errore", "Nessun file selezionato.")
        return
    target_language = simpledialog.askstring("Lingua di destinazione", "Inserisci la lingua di destinazione (es. 'it' per italiano):")
    if not target_language:
        messagebox.showerror("Errore", "Nessuna lingua selezionata.")
        return

    text = convert_pdf_to_text(pdf_path)
    translated_text = translate_text(text, target_language)

    file_format = simpledialog.askstring("Formato di salvataggio", "Inserisci il formato di salvataggio (txt, latex, markdown):")
    if file_format not in ['txt', 'latex', 'markdown']:
        messagebox.showerror("Errore", "Formato di salvataggio non valido.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=f".{file_format}", filetypes=[(f"{file_format.upper()} files", f"*.{file_format}")])
    if not save_path:
        messagebox.showerror("Errore", "Nessun percorso di salvataggio selezionato.")
        return

    save_translated_text(translated_text, save_path, file_format)
    messagebox.showinfo("Successo", "Documento tradotto salvato con successo.")

if __name__ == '__main__':
    main()
