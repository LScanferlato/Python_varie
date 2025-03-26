import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from datetime import datetime, date
import math

class PianetaOrbitale:
    def __init__(self, nome, distanza_dal_sole, periodo_orbitale, colore, 
                 inclinazione_orbitale=0, longitudine_nodo_ascendente=0):
        """
        Inizializza un pianeta con le sue caratteristiche orbitali più dettagliate.
        
        :param nome: Nome del pianeta
        :param distanza_dal_sole: Distanza media dal sole in unità astronomiche (UA)
        :param periodo_orbitale: Periodo orbitale in anni terrestri
        :param colore: Colore per la visualizzazione dell'orbita
        :param inclinazione_orbitale: Inclinazione dell'orbita rispetto al piano dell'eclittica
        :param longitudine_nodo_ascendente: Longitudine del nodo ascendente
        """
        self.nome = nome
        self.distanza = distanza_dal_sole
        self.periodo = periodo_orbitale
        self.colore = colore
        self.inclinazione = math.radians(inclinazione_orbitale)
        self.longitudine_nodo = math.radians(longitudine_nodo_ascendente)
    
    def calcola_posizione_attuale(self):
        """
        Calcola la posizione 3D attuale del pianeta nella sua orbita.
        
        :return: Coordinate x, y, z della posizione corrente
        """
        # Data di riferimento (epoche standard degli elementi orbitali)
        data_rif = date(2000, 1, 1)
        data_oggi = date.today()
        
        # Calcola i giorni trascorsi dalla data di riferimento
        giorni_trascorsi = (data_oggi - data_rif).days
        
        # Calcola l'angolo di movimento medio
        giorni_in_anno = 365.25
        movimento_medio = (giorni_trascorsi / (giorni_in_anno * self.periodo)) * (2 * np.pi)
        
        # Calcola le coordinate nel piano dell'orbita
        theta = movimento_medio
        x_piano = self.distanza * np.cos(theta)
        y_piano = self.distanza * np.sin(theta)
        
        # Applica rotazione per inclinazione e nodo ascendente
        # Matrice di rotazione 3D
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

def visualizza_sistema_solare_3d():
    """
    Visualizza le orbite dei pianeti del sistema solare in 3D con posizione attuale.
    """
    # Definizione dei pianeti con nome, distanza, periodo, colore, 
    # inclinazione orbitale e longitudine del nodo ascendente
    pianeti = [
        PianetaOrbitale("Mercurio", 0.39, 0.24, "gray", 7.005, 48.331),
        PianetaOrbitale("Venere", 0.72, 0.62, "orange", 3.39458, 76.680),
        PianetaOrbitale("Terra", 1.00, 1.00, "blue", 0.00, -11.26064),
        PianetaOrbitale("Marte", 1.52, 1.88, "red", 1.850, 49.557),
        PianetaOrbitale("Giove", 5.20, 11.86, "brown", 1.303, 100.464),
        PianetaOrbitale("Saturno", 9.54, 29.46, "gold", 2.485, 113.665),
        PianetaOrbitale("Urano", 19.22, 84.01, "lightblue", 0.773, 74.006),
        PianetaOrbitale("Nettuno", 30.06, 164.79, "darkblue", 1.767, 131.784)
    ]
    
    # Configurazione del grafico 3D
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(111, projection='3d')
    
    # Titolo con data corrente
    plt.title(f"Orbite dei Pianeti del Sistema Solare al {datetime.now().strftime('%d/%m/%Y')}", 
              fontsize=16)
    
    # Disegna il Sole al centro
    ax.scatter(0, 0, 0, color='yellow', s=300, label='Sole', zorder=10, 
               edgecolor='black', linewidth=1)
    
    # Disegna le orbite di ciascun pianeta
    for pianeta in pianeti:
        # Calcola orbita 3D
        x_orbita, y_orbita, z_orbita = pianeta.calcola_orbita_3d()
        
        # Disegna l'orbita
        ax.plot(x_orbita, y_orbita, z_orbita, color=pianeta.colore, 
                label=f"{pianeta.nome} (Periodo: {pianeta.periodo} anni)", 
                linewidth=2, linestyle='--', alpha=0.7)
        
        # Calcola e disegna la posizione attuale
        x_pos, y_pos, z_pos = pianeta.calcola_posizione_attuale()
        ax.scatter(x_pos, y_pos, z_pos, color=pianeta.colore, s=200, zorder=10, 
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

# Esegui la visualizzazione
if __name__ == "__main__":
    visualizza_sistema_solare_3d()
