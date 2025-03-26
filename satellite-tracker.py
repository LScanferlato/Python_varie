import requests
import folium
from folium.plugins import MarkerCluster
from skyfield.api import load, Topos
from skyfield.sgp4lib import EarthSatellite
from datetime import datetime, timedelta
import time
import math

class SatelliteTracker:
    def __init__(self):
        # Carica il file di effemeridi
        self.ts = load.timescale()
        
        # Definisci i gruppi di satelliti con colori corrispondenti
        self.satellite_sources = {
            'Communications': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=iridium',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=iridium-NEXT',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=globalstar',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=amateur',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=swarm'
                ],
                'color': 'blue'
            },
            'Weather': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=weather',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=noaa'
                ],
                'color': 'red'
            },
            'Navigation': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=gps-ops',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=glonass-ops',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=galileo',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=musson'
                ],
                'color': 'green'
            },
            'Earth Observation': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=resource',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=earth-obs'
                ],
                'color': 'purple'
            },
            'Miscellaneous Satellites': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=military',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=radar',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=cubesat',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=other'
                ],
                'color': 'yellow'
            },
            'Scientific Satellites': {
                'urls': [
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=geodetic',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=engineering',
                    'https://celestrak.org/NORAD/elements/gp.php?GROUP=education'
                ],
                'color': 'green'
            }
        }
        
        # Dizionario per memorizzare i satelliti
        self.satellites = {}
        
    def is_valid_coordinate(self, latitude, longitude):
        """
        Verifica se le coordinate sono valide:
        - Non sono NaN
        - Latitudine è tra -90 e 90
        - Longitudine è tra -180 e 180
        """
        return (not math.isnan(latitude) and 
                not math.isnan(longitude) and 
                -90 <= latitude <= 90 and 
                -180 <= longitude <= 180)
    
    def download_tle_data(self):
        """Scarica i dati TLE per diversi gruppi di satelliti"""
        self.satellites.clear()
        
        for group_name, group_info in self.satellite_sources.items():
            for url in group_info['urls']:
                try:
                    response = requests.get(url)
                    tle_data = response.text.splitlines()
                    
                    # Parsing dei dati TLE
                    for i in range(0, len(tle_data), 3):
                        if i+2 < len(tle_data):
                            name = tle_data[i].strip()
                            line1 = tle_data[i+1].strip()
                            line2 = tle_data[i+2].strip()
                            
                            try:
                                # Utilizzare EarthSatellite per creare i satelliti
                                satellite = EarthSatellite(line1, line2, name, self.ts)
                                # Aggiungi un campo per il gruppo e il colore
                                satellite.group = group_name
                                satellite.color = group_info['color']
                                self.satellites[name] = satellite
                            except Exception as e:
                                print(f"Errore nel parsing del satellite {name}: {e}")
                
                except Exception as e:
                    print(f"Errore nel download dei dati TLE dall'URL {url}: {e}")
        
        print(f"Caricati {len(self.satellites)} satelliti")
    
    def create_satellite_map(self):
        """Crea una mappa interattiva con le posizioni dei satelliti raggruppate"""
        # Crea una mappa centrata sull'Italia
        m = folium.Map(
            location=[42.5, 12.5],  # Coordinate centrali dell'Italia
            zoom_start=6  # Zoom ottimale per vedere tutta l'Italia
        )
        
        # Dizionario per i cluster dei gruppi
        group_clusters = {}
        
        # Calcola la posizione corrente di ogni satellite
        now = self.ts.now()
        
        # Conta i satelliti posizionati con successo
        satelliti_posizionati = 0
        
        # Crea un cluster per ogni gruppo
        for group_name, group_info in self.satellite_sources.items():
            group_clusters[group_name] = MarkerCluster(
                name=group_name,
                overlay=True,
                control=True,
                icon_create_function=None
            )
            group_clusters[group_name].add_to(m)
        
        for name, satellite in self.satellites.items():
            try:
                # Calcola la posizione del satellite
                geocentric = satellite.at(now)
                subpoint = geocentric.subpoint()
                
                # Ottieni latitudine e longitudine
                latitude = subpoint.latitude.degrees
                longitude = subpoint.longitude.degrees
                
                # Verifica validità delle coordinate
                if self.is_valid_coordinate(latitude, longitude):
                    # Crea un popup con informazioni dettagliate
                    popup_text = f"""
                    <b>Nome:</b> {name}<br>
                    <b>Gruppo:</b> {satellite.group}<br>
                    <b>Lat:</b> {latitude:.4f}°<br>
                    <b>Lon:</b> {longitude:.4f}°
                    """
                    
                    # Aggiungi un marker al cluster corrispondente
                    folium.CircleMarker(
                        location=[latitude, longitude],
                        radius=5,
                        popup=popup_text,
                        color=satellite.color,
                        fill=True,
                        fillColor=satellite.color
                    ).add_to(group_clusters[satellite.group])
                    
                    satelliti_posizionati += 1
                else:
                    print(f"Coordinate non valide per {name}: lat={latitude}, lon={longitude}")
            
            except Exception as e:
                print(f"Errore nel posizionamento del satellite {name}: {e}")
        
        # Aggiungi il controllo dei layer
        folium.LayerControl().add_to(m)
        
        # Salva la mappa
        m.save('satellite_tracker_map.html')
        print(f"Mappa dei satelliti salvata. Satelliti posizionati: {satelliti_posizionati}")
    
    def track_satellites_realtime(self, update_interval=300):
        """Traccia i satelliti in tempo reale con aggiornamenti periodici"""
        try:
            while True:
                # Scarica i dati più recenti
                self.download_tle_data()
                
                # Crea la mappa
                self.create_satellite_map()
                
                # Attendi prima del prossimo aggiornamento
                print(f"Prossimo aggiornamento tra {update_interval} secondi")
                time.sleep(update_interval)
        
        except KeyboardInterrupt:
            print("\nTracciamento satelliti interrotto.")
        except Exception as e:
            print(f"Errore nel tracciamento dei satelliti: {e}")

def main():
    # Inizializza il tracker
    tracker = SatelliteTracker()
    
    # Avvia il tracciamento in tempo reale
    tracker.track_satellites_realtime()

if __name__ == "__main__":
    main()

# Requisiti (da installare con pip):
# skyfield
# folium
# requests
