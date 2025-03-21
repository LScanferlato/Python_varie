import requests
import subprocess

# Ottieni i tassi di cambio odierni
url = "https://api.exchangerate-api.com/v4/latest/EUR"
response = requests.get(url)
data = response.json()

# Crea la tabella in LaTeX
latex_table = r"""
\documentclass{article}
\usepackage[table]{xcolor}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\begin{document}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}|c|c|}
\hline
\rowcolors{1}{gray!20}{green!20}
Valuta & Tasso di Cambio \\
\hline
"""

for currency, rate in data['rates'].items():
    latex_table += f"{currency} & {rate} \\\\ \n"

latex_table += r"""
\hline
\end{tabular*}
\end{document}
"""

# Salva la tabella in un file .tex
with open("exchange_rates_table.tex", "w") as file:
    file.write(latex_table)

# Compila il file .tex in PDF
subprocess.run(["pdflatex", "exchange_rates_table.tex"])

print("Tabella LaTeX creata e salvata come PDF con successo!")
