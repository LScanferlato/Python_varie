import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# URL per recuperare i dati sulle tempeste geomagnetiche
url = "https://services.swpc.noaa.gov/products/solar-wind/mag-7-day.json"

# Recupera i dati
response = requests.get(url)

# Verifica se la richiesta è stata eseguita con successo
if response.status_code == 200:
    # Carica i dati JSON
    data = json.loads(response.text)
    
    # Verifica se i dati sono una lista di liste
    if isinstance(data, list) and all(isinstance(item, list) for item in data):
        # Estrae le intestazioni e i dati
        headers = data[0]
        data_rows = data[1:]
        
        # Crea un dizionario per ogni riga di dati
        data_dicts = [dict(zip(headers, row)) for row in data_rows]
        
        # Estrae le date e i valori di Bz (componente z della forza magnetica)
        dates = [dt.datetime.strptime(item['time_tag'], '%Y-%m-%d %H:%M:%S.%f') for item in data_dicts]
        bz_values = [item['bz_gsm'] for item in data_dicts]
        
        # Crea il grafico
        plt.figure(figsize=(12, 6))
        plt.plot(dates, bz_values, label='Bz (nT)')
        
        # Formatta le date sull'asse x
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        plt.gcf().autofmt_xdate()
        
        # Aggiungi titolo e label agli assi
        plt.title('Tempeste Geomagnetiche - Valori di Bz')
        plt.xlabel('Data')
        plt.ylabel('Bz (nT)')
        plt.legend()
        
        # Mostra il grafico
        plt.show()
    else:
        print("I dati non sono nel formato previsto.")
else:
    print("Errore nel recuperare i dati:", response.status_code)
