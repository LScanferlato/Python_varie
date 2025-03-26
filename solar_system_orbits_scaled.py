import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime, date, timedelta
import math

class PianetaOrbitale:
    def __init__(self, nome, distanza_dal_sole, periodo_orbitale, colore, 
                 raggio_pianeta, inclinazione_orbitale=0, longitudine_nodo_ascendente=0):
        """
        Inizializza un pianeta con caratteristiche orbitali e fisiche dettagliate.
        
        :param nome: Nome del pianeta
        :param distanza_dal_sole: Distanza media dal sole in unità astronomiche (UA)
        :param periodo_orbitale: Periodo orbitale in anni terrestri
        :param colore: Colore per la visualizzazione dell'orbita
        :param raggio_pianeta: Raggio del pianeta in km (per la scala)
        :param inclinazione_orbitale: Inclinazione dell'orbita rispetto al piano dell'eclittica
        :param longitudine_nodo_ascendente: Longitudine del nodo ascendente
        """
        self.nome = nome
        self.distanza = distanza_dal_sole
        self.periodo = periodo_orbitale
        self.colore = colore
        self.raggio = raggio_pianeta  # Raggio in km
        self.inclinazione = math.radians(inclinazione_orbitale)
        self.longitudine_nodo = math.radians(longitudine_nodo_ascendente)
    
    def calcola_posizione(self, giorni_da_riferimento):
        """
        Calcola la posizione 3D del pianeta in un dato momento.
        
        :param giorni_da_riferimento: Giorni trascorsi dalla data di riferimento
        :return: Coordinate x, y, z della posizione
        """
        # Calcola l'angolo di movimento medio
        giorni_in_anno = 365.25
        movimento_medio = (giorni_da_riferimento / (giorni_in_anno * self.periodo)) * (2 * np.pi)
        
        # Calcola le coordinate nel piano dell'orbita
        theta = movimento_medio
        x_piano = self.distanza * np.cos(theta)
        y_piano = self.distanza * np.sin(theta)
        
        # Applica rotazione per inclinazione e nodo ascendente
        cos_i = np.cos(self.inclinazione)
        sin_i = np.sin(self.inclinazione)
        cos_nodo = np.cos(self.longitudine_nodo)
        sin_nodo = np.sin(self.longitudine_nodo)
        
        x = (cos_nodo * x_piano - sin_nodo * y_piano * cos_i)
        y = (sin_nodo * x_piano + cos_nodo * y_piano * cos_i)
        z = (y_piano * sin_i)
        
        return x, y, z
    
    def calcola_orbita_3d(self, num_punti=1000):
        """
        Calcola i punti dell'orbita 3D del pianeta.
        
        :param num_punti: Numero di punti per disegnare l'orbita
        :return: Coordinate x, y, z dell'orbita
        """
        # Genera punti nel piano dell'orbita
        theta = np.linspace(0, 2*np.pi, num_punti)
        x_piano = self.distanza * np.cos(theta)
        y_piano = self.distanza * np.sin(theta)
        
        # Applica rotazione 3D
        cos_i = np.cos(self.inclinazione)
        sin_i = np.sin(self.inclinazione)
        cos_nodo = np.cos(self.longitudine_nodo)
        sin_nodo = np.sin(self.longitudine_nodo)
        
        x = cos_nodo * x_piano - sin_nodo * y_piano * cos_i
        y = sin_nodo * x_piano + cos_nodo * y_piano * cos_i
        z = y_piano * sin_i
        
        return x, y, z

def visualizza_sistema_solare_3d(data_simulazione=None, giorni_da_riferimento=None):
    """
    Visualizza le orbite dei pianeti del sistema solare in 3D con scala e simulazione temporale.
    
    :param data_simulazione: Data specifica per la simulazione
    :param giorni_da_riferimento: Giorni trascorsi dalla data di riferimento
    """
    # Data di riferimento (epoche standard degli elementi orbitali)
    data_rif = date(2000, 1, 1)
    
    # Determina i giorni da utilizzare
    if giorni_da_riferimento is not None:
        # Usa giorni passati come parametro
        giorni = giorni_da_riferimento
    elif data_simulazione is not None:
        # Calcola giorni dalla data di simulazione
        giorni = (data_simulazione - data_rif).days
    else:
        # Usa la data corrente come default
        giorni = (date.today() - data_rif).days
    
    # Definizione dei pianeti con nome, distanza, periodo, colore, raggio, 
    # inclinazione orbitale e longitudine del nodo ascendente
    pianeti = [
        PianetaOrbitale("Mercurio", 0.39, 0.24, "gray", 2440, 7.005, 48.331),
        PianetaOrbitale("Venere", 0.72, 0.62, "orange", 6052, 3.39458, 76.680),
        PianetaOrbitale("Terra", 1.00, 1.00, "blue", 6371, 0.00, -11.26064),
        PianetaOrbitale("Marte", 1.52, 1.88, "red", 3390, 1.850, 49.557),
        PianetaOrbitale("Giove", 5.20, 11.86, "brown", 69911, 1.303, 100.464),
        PianetaOrbitale("Saturno", 9.54, 29.46, "gold", 58232, 2.485, 113.665),
        PianetaOrbitale("Urano", 19.22, 84.01, "lightblue", 25362, 0.773, 74.006),
        PianetaOrbitale("Nettuno", 30.06, 164.79, "darkblue", 24622, 1.767, 131.784)
    ]
    
    # Configurazione del grafico 3D
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Titolo con data di simulazione
    data_visualizzata = data_rif + timedelta(days=giorni)
    plt.title(f"Orbite dei Pianeti del Sistema Solare al {data_visualizzata.strftime('%d/%m/%Y')}", 
              fontsize=16)
    
    # Scala dei raggi planetari (log scale per rendere visibili pianeti piccoli)
    raggi_scala = np.log10(np.array([p.raggio for p in pianeti]))
    raggi_normalizzati = 100 * (raggi_scala - raggi_scala.min()) / (raggi_scala.max() - raggi_scala.min()) + 10
    
    # Disegna il Sole al centro (scala log per essere visibile)
    ax.scatter(0, 0, 0, color='yellow', s=500, label='Sole', zorder=10, 
               edgecolor='black', linewidth=1)
    
    # Disegna le orbite di ciascun pianeta
    for i, pianeta in enumerate(pianeti):
        # Calcola orbita 3D
        x_orbita, y_orbita, z_orbita = pianeta.calcola_orbita_3d()
        
        # Disegna l'orbita
        ax.plot(x_orbita, y_orbita, z_orbita, color=pianeta.colore, 
                label=f"{pianeta.nome} (Raggio: {pianeta.raggio} km)", 
                linewidth=2, linestyle='--', alpha=0.7)
        
        # Calcola e disegna la posizione
        x_pos, y_pos, z_pos = pianeta.calcola_posizione(giorni)
        ax.scatter(x_pos, y_pos, z_pos, color=pianeta.colore, s=raggi_normalizzati[i], zorder=10, 
                   edgecolor='black', linewidth=1)
        
        # Aggiungi etichetta con il nome del pianeta
        ax.text(x_pos, y_pos, z_pos, pianeta.nome, fontsize=9)
    
    # Imposta etichette degli assi
    ax.set_xlabel('X (UA)')
    ax.set_ylabel('Y (UA)')
    ax.set_zlabel('Z (UA)')
    
    # Imposta limiti degli assi per una visualizzazione simmetrica
    max_dist = max(pianeta.distanza for pianeta in pianeti)
    ax.set_xlim(-max_dist*1.2, max_dist*1.2)
    ax.set_ylim(-max_dist*1.2, max_dist*1.2)
    ax.set_zlim(-max_dist*1.2, max_dist*1.2)
    
    # Aggiungi legenda
    ax.legend(loc='best', title='Pianeti', fontsize=8)
    
    # Abilita l'interazione
    plt.tight_layout()
    
    # Mostra il grafico
    plt.show()

# Funzione per eseguire simulazioni
def simula_sistema_solare():
    """
    Interfaccia per eseguire diverse simulazioni del sistema solare.
    """
    while True:
        print("\nSimulazione del Sistema Solare")
        print("1. Posizione attuale")
        print("2. Seleziona data specifica")
        print("3. Simula giorni da data di riferimento")
        print("4. Esci")
        
        scelta = input("Scegli un'opzione (1-4): ")
        
        try:
            if scelta == '1':
                visualizza_sistema_solare_3d()
            elif scelta == '2':
                # Richiedi data specifica
                anno = int(input("Inserisci l'anno (AAAA): "))
                mese = int(input("Inserisci il mese (1-12): "))
                giorno = int(input("Inserisci il giorno (1-31): "))
                data_sim = date(anno, mese, giorno)
                visualizza_sistema_solare_3d(data_simulazione=data_sim)
            elif scelta == '3':
                # Simula per giorni da data di riferimento
                giorni = int(input("Inserisci il numero di giorni da data di riferimento (1 gennaio 2000): "))
                visualizza_sistema_solare_3d(giorni_da_riferimento=giorni)
            elif scelta == '4':
                break
            else:
                print("Scelta non valida. Riprova.")
        except ValueError:
            print("Input non valido. Riprova.")

# Esegui la simulazione
if __name__ == "__main__":
    simula_sistema_solare()
