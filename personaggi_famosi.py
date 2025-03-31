import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Lista di personaggi famosi con le loro date di nascita e morte, città natale e di morte
personaggi = [
    {"nome": "Albert Einstein", "nascita": "1879-03-14", "morte": "1955-04-18", "città_nascita": "Ulm", "città_morte": "Princeton"},
    {"nome": "Marie Curie", "nascita": "1867-11-07", "morte": "1934-07-04", "città_nascita": "Varsavia", "città_morte": "Sallanches"},
    {"nome": "Isaac Newton", "nascita": "1643-01-04", "morte": "1727-03-31", "città_nascita": "Woolsthorpe", "città_morte": "Kensington"},
    {"nome": "Leonardo da Vinci", "nascita": "1452-04-15", "morte": "1519-05-02", "città_nascita": "Vinci", "città_morte": "Amboise"},
    {"nome": "Galileo Galilei", "nascita": "1564-02-15", "morte": "1642-01-08", "città_nascita": "Pisa", "città_morte": "Arcetri"},
    {"nome": "Charles Darwin", "nascita": "1809-02-12", "morte": "1882-04-19", "città_nascita": "Shrewsbury", "città_morte": "Downe"},
    {"nome": "Nikola Tesla", "nascita": "1856-07-10", "morte": "1943-01-07", "città_nascita": "Smiljan", "città_morte": "New York"},
    {"nome": "Ada Lovelace", "nascita": "1815-12-10", "morte": "1852-11-27", "città_nascita": "Londra", "città_morte": "Londra"},
    {"nome": "Alan Turing", "nascita": "1912-06-23", "morte": "1954-06-07", "città_nascita": "Londra", "città_morte": "Wilmslow"},
    {"nome": "Stephen Hawking", "nascita": "1942-01-08", "morte": "2018-03-14", "città_nascita": "Oxford", "città_morte": "Cambridge"},
    # Imperatori romani
    {"nome": "Augusto", "nascita": "-0063-03-15", "morte": "0014-08-19", "città_nascita": "Roma", "città_morte": "Nola"},
    {"nome": "Tiberio", "nascita": "-0042-11-16", "morte": "0037-03-16", "città_nascita": "Roma", "città_morte": "Miseno"},
    {"nome": "Caligola", "nascita": "0012-08-31", "morte": "0041-01-24", "città_nascita": "Anzio", "città_morte": "Roma"},
    {"nome": "Nerone", "nascita": "0037-12-15", "morte": "0068-06-09", "città_nascita": "Anzio", "città_morte": "Roma"},
    {"nome": "Traiano", "nascita": "0053-09-18", "morte": "0117-08-08", "città_nascita": "Italica", "città_morte": "Selinus"},
    # Sovrani greci
    {"nome": "Alessandro Magno", "nascita": "-0356-07-20", "morte": "-0323-06-10", "città_nascita": "Pella", "città_morte": "Babilonia"},
    {"nome": "Pericle", "nascita": "-0495-01-01", "morte": "-0429-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Leonida I", "nascita": "-0540-01-01", "morte": "-0480-01-01", "città_nascita": "Sparta", "città_morte": "Termopili"},
    {"nome": "Filippo II di Macedonia", "nascita": "-0382-01-01", "morte": "-0336-01-01", "città_nascita": "Pella", "città_morte": "Aigai"},
    # Re e imperatori europei
    {"nome": "Carlo Magno", "nascita": "0747-04-02", "morte": "0814-01-28", "città_nascita": "Aquisgrana", "città_morte": "Aquisgrana"},
    {"nome": "Federico Barbarossa", "nascita": "1122-01-01", "morte": "1190-06-10", "città_nascita": "Haguenau", "città_morte": "Saleph"},
    {"nome": "Napoleone Bonaparte", "nascita": "1769-08-15", "morte": "1821-05-05", "città_nascita": "Ajaccio", "città_morte": "Sant'Elena"},
    {"nome": "Elisabetta I", "nascita": "1533-09-07", "morte": "1603-03-24", "città_nascita": "Greenwich", "città_morte": "Richmond"},
        # 100 nuovi personaggi famosi aggiunti
    # Filosofi e pensatori
    {"nome": "Socrate", "nascita": "-0469-01-01", "morte": "-0399-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Platone", "nascita": "-0427-01-01", "morte": "-0347-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Aristotele", "nascita": "-0384-01-01", "morte": "-0322-01-01", "città_nascita": "Stagira", "città_morte": "Calcide"},
    {"nome": "Confucio", "nascita": "-0551-09-28", "morte": "-0479-04-11", "città_nascita": "Qufu", "città_morte": "Qufu"},
    {"nome": "Immanuel Kant", "nascita": "1724-04-22", "morte": "1804-02-12", "città_nascita": "Königsberg", "città_morte": "Königsberg"},
    {"nome": "Friedrich Nietzsche", "nascita": "1844-10-15", "morte": "1900-08-25", "città_nascita": "Röcken", "città_morte": "Weimar"},
    {"nome": "Jean-Jacques Rousseau", "nascita": "1712-06-28", "morte": "1778-07-02", "città_nascita": "Ginevra", "città_morte": "Ermenonville"},
    {"nome": "René Descartes", "nascita": "1596-03-31", "morte": "1650-02-11", "città_nascita": "La Haye en Touraine", "città_morte": "Stoccolma"},
    
    # Scienziati e inventori
    {"nome": "Thomas Edison", "nascita": "1847-02-11", "morte": "1931-10-18", "città_nascita": "Milan", "città_morte": "West Orange"},
    {"nome": "Alexander Graham Bell", "nascita": "1847-03-03", "morte": "1922-08-02", "città_nascita": "Edimburgo", "città_morte": "Beinn Bhreagh"},
    {"nome": "Enrico Fermi", "nascita": "1901-09-29", "morte": "1954-11-28", "città_nascita": "Roma", "città_morte": "Chicago"},
    {"nome": "Guglielmo Marconi", "nascita": "1874-04-25", "morte": "1937-07-20", "città_nascita": "Bologna", "città_morte": "Roma"},
    {"nome": "Louis Pasteur", "nascita": "1822-12-27", "morte": "1895-09-28", "città_nascita": "Dole", "città_morte": "Marnes-la-Coquette"},
    {"nome": "Antoine Lavoisier", "nascita": "1743-08-26", "morte": "1794-05-08", "città_nascita": "Parigi", "città_morte": "Parigi"},
    {"nome": "Rachel Carson", "nascita": "1907-05-27", "morte": "1964-04-14", "città_nascita": "Springdale", "città_morte": "Silver Spring"},
    {"nome": "Max Planck", "nascita": "1858-04-23", "morte": "1947-10-04", "città_nascita": "Kiel", "città_morte": "Göttingen"},
    {"nome": "Lise Meitner", "nascita": "1878-11-07", "morte": "1968-10-27", "città_nascita": "Vienna", "città_morte": "Cambridge"},
    {"nome": "Richard Feynman", "nascita": "1918-05-11", "morte": "1988-02-15", "città_nascita": "New York", "città_morte": "Los Angeles"},
    
    # Artisti e scrittori
    {"nome": "William Shakespeare", "nascita": "1564-04-26", "morte": "1616-04-23", "città_nascita": "Stratford-upon-Avon", "città_morte": "Stratford-upon-Avon"},
    {"nome": "Michelangelo", "nascita": "1475-03-06", "morte": "1564-02-18", "città_nascita": "Caprese", "città_morte": "Roma"},
    {"nome": "Vincent van Gogh", "nascita": "1853-03-30", "morte": "1890-07-29", "città_nascita": "Zundert", "città_morte": "Auvers-sur-Oise"},
    {"nome": "Pablo Picasso", "nascita": "1881-10-25", "morte": "1973-04-08", "città_nascita": "Málaga", "città_morte": "Mougins"},
    {"nome": "Johann Wolfgang von Goethe", "nascita": "1749-08-28", "morte": "1832-03-22", "città_nascita": "Francoforte", "città_morte": "Weimar"},
    {"nome": "Virginia Woolf", "nascita": "1882-01-25", "morte": "1941-03-28", "città_nascita": "Londra", "città_morte": "Lewes"},
    {"nome": "Frida Kahlo", "nascita": "1907-07-06", "morte": "1954-07-13", "città_nascita": "Coyoacán", "città_morte": "Coyoacán"},
    {"nome": "Claude Monet", "nascita": "1840-11-14", "morte": "1926-12-05", "città_nascita": "Parigi", "città_morte": "Giverny"},
    {"nome": "Marcel Proust", "nascita": "1871-07-10", "morte": "1922-11-18", "città_nascita": "Auteuil", "città_morte": "Parigi"},
    {"nome": "Jane Austen", "nascita": "1775-12-16", "morte": "1817-07-18", "città_nascita": "Steventon", "città_morte": "Winchester"},
    {"nome": "Edgar Allan Poe", "nascita": "1809-01-19", "morte": "1849-10-07", "città_nascita": "Boston", "città_morte": "Baltimora"},
    {"nome": "Oscar Wilde", "nascita": "1854-10-16", "morte": "1900-11-30", "città_nascita": "Dublino", "città_morte": "Parigi"},

    # Personaggi politici e leader
    {"nome": "Mahatma Gandhi", "nascita": "1869-10-02", "morte": "1948-01-30", "città_nascita": "Porbandar", "città_morte": "Nuova Delhi"},
    {"nome": "Nelson Mandela", "nascita": "1918-07-18", "morte": "2013-12-05", "città_nascita": "Mvezo", "città_morte": "Johannesburg"},
    {"nome": "Abraham Lincoln", "nascita": "1809-02-12", "morte": "1865-04-15", "città_nascita": "Hodgenville", "città_morte": "Washington D.C."},
    {"nome": "Winston Churchill", "nascita": "1874-11-30", "morte": "1965-01-24", "città_nascita": "Woodstock", "città_morte": "Londra"},
    {"nome": "Giovanna d'Arco", "nascita": "1412-01-06", "morte": "1431-05-30", "città_nascita": "Domrémy", "città_morte": "Rouen"},
    {"nome": "Cleopatra", "nascita": "-0069-01-01", "morte": "-0030-08-01", "città_nascita": "Alessandria", "città_morte": "Alessandria"},
    {"nome": "Martin Luther King Jr.", "nascita": "1929-01-15", "morte": "1968-04-04", "città_nascita": "Atlanta", "città_morte": "Memphis"},
    {"nome": "Catherine de' Medici", "nascita": "1519-04-13", "morte": "1589-01-05", "città_nascita": "Firenze", "città_morte": "Blois"},
    {"nome": "Simón Bolívar", "nascita": "1783-07-24", "morte": "1830-12-17", "città_nascita": "Caracas", "città_morte": "Santa Marta"},
    {"nome": "Catherine the Great", "nascita": "1729-05-02", "morte": "1796-11-17", "città_nascita": "Stettino", "città_morte": "San Pietroburgo"},
    
    # Musicisti
    {"nome": "Ludwig van Beethoven", "nascita": "1770-12-17", "morte": "1827-03-26", "città_nascita": "Bonn", "città_morte": "Vienna"},
    {"nome": "Wolfgang Amadeus Mozart", "nascita": "1756-01-27", "morte": "1791-12-05", "città_nascita": "Salisburgo", "città_morte": "Vienna"},
    {"nome": "Johann Sebastian Bach", "nascita": "1685-03-31", "morte": "1750-07-28", "città_nascita": "Eisenach", "città_morte": "Lipsia"},
    {"nome": "Frédéric Chopin", "nascita": "1810-03-01", "morte": "1849-10-17", "città_nascita": "Żelazowa Wola", "città_morte": "Parigi"},
    {"nome": "Louis Armstrong", "nascita": "1901-08-04", "morte": "1971-07-06", "città_nascita": "New Orleans", "città_morte": "New York"},
    {"nome": "Elvis Presley", "nascita": "1935-01-08", "morte": "1977-08-16", "città_nascita": "Tupelo", "città_morte": "Memphis"},
    {"nome": "Ella Fitzgerald", "nascita": "1917-04-25", "morte": "1996-06-15", "città_nascita": "Newport News", "città_morte": "Beverly Hills"},
    {"nome": "Bob Marley", "nascita": "1945-02-06", "morte": "1981-05-11", "città_nascita": "Nine Mile", "città_morte": "Miami"},
    {"nome": "Maria Callas", "nascita": "1923-12-02", "morte": "1977-09-16", "città_nascita": "New York", "città_morte": "Parigi"},
    {"nome": "Giuseppe Verdi", "nascita": "1813-10-10", "morte": "1901-01-27", "città_nascita": "Roncole", "città_morte": "Milano"},
    
    # Altri imperatori romani
    {"nome": "Giulio Cesare", "nascita": "-0100-07-12", "morte": "-0044-03-15", "città_nascita": "Roma", "città_morte": "Roma"},
    {"nome": "Marco Aurelio", "nascita": "0121-04-26", "morte": "0180-03-17", "città_nascita": "Roma", "città_morte": "Vindobona"},
    {"nome": "Adriano", "nascita": "0076-01-24", "morte": "0138-07-10", "città_nascita": "Italica", "città_morte": "Baia"},
    {"nome": "Costantino", "nascita": "0272-02-27", "morte": "0337-05-22", "città_nascita": "Naissus", "città_morte": "Nicomedia"},
    {"nome": "Diocleziano", "nascita": "0244-12-22", "morte": "0311-12-03", "città_nascita": "Salona", "città_morte": "Spalato"},
    
    # Altri esploratori e navigatori
    {"nome": "Cristoforo Colombo", "nascita": "1451-10-31", "morte": "1506-05-20", "città_nascita": "Genova", "città_morte": "Valladolid"},
    {"nome": "Marco Polo", "nascita": "1254-09-15", "morte": "1324-01-08", "città_nascita": "Venezia", "città_morte": "Venezia"},
    {"nome": "Vasco da Gama", "nascita": "1469-01-01", "morte": "1524-12-24", "città_nascita": "Sines", "città_morte": "Cochin"},
    {"nome": "Ferdinando Magellano", "nascita": "1480-02-03", "morte": "1521-04-27", "città_nascita": "Sabrosa", "città_morte": "Mactan"},
    {"nome": "James Cook", "nascita": "1728-11-07", "morte": "1779-02-14", "città_nascita": "Marton", "città_morte": "Kealakekua Bay"},
    {"nome": "Amerigo Vespucci", "nascita": "1454-03-09", "morte": "1512-02-22", "città_nascita": "Firenze", "città_morte": "Siviglia"},
    {"nome": "Roald Amundsen", "nascita": "1872-07-16", "morte": "1928-06-18", "città_nascita": "Borge", "città_morte": "Mare di Barents"},
    {"nome": "Ibn Battuta", "nascita": "1304-02-25", "morte": "1369-01-01", "città_nascita": "Tangeri", "città_morte": "Marrakech"},
    
    # Scienziati e inventori moderni
    {"nome": "Rosalind Franklin", "nascita": "1920-07-25", "morte": "1958-04-16", "città_nascita": "Londra", "città_morte": "Londra"},
    {"nome": "Alexander Fleming", "nascita": "1881-08-06", "morte": "1955-03-11", "città_nascita": "Ayrshire", "città_morte": "Londra"},
    {"nome": "James Watt", "nascita": "1736-01-19", "morte": "1819-08-25", "città_nascita": "Greenock", "città_morte": "Handsworth"},
    {"nome": "Annie Jump Cannon", "nascita": "1863-12-11", "morte": "1941-04-13", "città_nascita": "Dover", "città_morte": "Cambridge"},
    {"nome": "Carl Sagan", "nascita": "1934-11-09", "morte": "1996-12-20", "città_nascita": "Brooklyn", "città_morte": "Seattle"},
    {"nome": "John von Neumann", "nascita": "1903-12-28", "morte": "1957-02-08", "città_nascita": "Budapest", "città_morte": "Washington D.C."},
    {"nome": "Grace Hopper", "nascita": "1906-12-09", "morte": "1992-01-01", "città_nascita": "New York", "città_morte": "Arlington"},
    {"nome": "James Clerk Maxwell", "nascita": "1831-06-13", "morte": "1879-11-05", "città_nascita": "Edimburgo", "città_morte": "Cambridge"},
    {"nome": "Marie-Anne Lavoisier", "nascita": "1758-01-20", "morte": "1836-02-10", "città_nascita": "Parigi", "città_morte": "Parigi"},
    {"nome": "Emmy Noether", "nascita": "1882-03-23", "morte": "1935-04-14", "città_nascita": "Erlangen", "città_morte": "Bryn Mawr"},
    {"nome": "Barbara McClintock", "nascita": "1902-06-16", "morte": "1992-09-02", "città_nascita": "Hartford", "città_morte": "Huntington"},
    {"nome": "Edwin Hubble", "nascita": "1889-11-20", "morte": "1953-09-28", "città_nascita": "Marshfield", "città_morte": "San Marino"},
    
    # Altri personaggi storici importanti
    {"nome": "Archimede", "nascita": "-0287-01-01", "morte": "-0212-01-01", "città_nascita": "Siracusa", "città_morte": "Siracusa"},
    {"nome": "Ippocrate", "nascita": "-0460-01-01", "morte": "-0370-01-01", "città_nascita": "Kos", "città_morte": "Larissa"},
    {"nome": "Pitagora", "nascita": "-0570-01-01", "morte": "-0495-01-01", "città_nascita": "Samo", "città_morte": "Metaponto"},
    {"nome": "Ibn Sina (Avicenna)", "nascita": "0980-08-23", "morte": "1037-06-21", "città_nascita": "Afshona", "città_morte": "Hamadan"},
    {"nome": "Ibn al-Haytham", "nascita": "0965-07-01", "morte": "1040-03-06", "città_nascita": "Bassora", "città_morte": "Il Cairo"},
    {"nome": "Al-Khwarizmi", "nascita": "0780-01-01", "morte": "0850-01-01", "città_nascita": "Corasmia", "città_morte": "Baghdad"},
    {"nome": "Sun Tzu", "nascita": "-0544-01-01", "morte": "-0496-01-01", "città_nascita": "Qi", "città_morte": "Wu"},
    {"nome": "Gutenberg", "nascita": "1400-01-01", "morte": "1468-02-03", "città_nascita": "Magonza", "città_morte": "Magonza"},
    
    # Pionieri dell'aviazione e dello spazio
    {"nome": "Fratelli Wright", "nascita": "1871-08-19", "morte": "1948-01-30", "città_nascita": "Millville", "città_morte": "Dayton"},
    {"nome": "Amelia Earhart", "nascita": "1897-07-24", "morte": "1937-07-02", "città_nascita": "Atchison", "città_morte": "Oceano Pacifico"},
    {"nome": "Jurij Gagarin", "nascita": "1934-03-09", "morte": "1968-03-27", "città_nascita": "Klušino", "città_morte": "Novosëlovo"},
    {"nome": "Neil Armstrong", "nascita": "1930-08-05", "morte": "2012-08-25", "città_nascita": "Wapakoneta", "città_morte": "Cincinnati"},
    {"nome": "Valentina Tereškova", "nascita": "1937-03-06", "morte": "2125-01-01", "città_nascita": "Maslennikovo", "città_morte": "-"},
    
    # Altri personaggi moderni di vari campi
    {"nome": "Charlie Chaplin", "nascita": "1889-04-16", "morte": "1977-12-25", "città_nascita": "Londra", "città_morte": "Corsier-sur-Vevey"},
    {"nome": "Walt Disney", "nascita": "1901-12-05", "morte": "1966-12-15", "città_nascita": "Chicago", "città_morte": "Burbank"},
    {"nome": "Albert Camus", "nascita": "1913-11-07", "morte": "1960-01-04", "città_nascita": "Mondovi", "città_morte": "Villeblevin"},
    {"nome": "Gabriel García Márquez", "nascita": "1927-03-06", "morte": "2014-04-17", "città_nascita": "Aracataca", "città_morte": "Città del Messico"},
    {"nome": "Ernest Hemingway", "nascita": "1899-07-21", "morte": "1961-07-02", "città_nascita": "Oak Park", "città_morte": "Ketchum"},
    {"nome": "Anne Frank", "nascita": "1929-06-12", "morte": "1945-03-01", "città_nascita": "Francoforte", "città_morte": "Bergen-Belsen"},
    {"nome": "Madre Teresa", "nascita": "1910-08-26", "morte": "1997-09-05", "città_nascita": "Skopje", "città_morte": "Calcutta"},
    {"nome": "Margaret Mead", "nascita": "1901-12-16", "morte": "1978-11-15", "città_nascita": "Filadelfia", "città_morte": "New York"},
    {"nome": "Sigmund Freud", "nascita": "1856-05-06", "morte": "1939-09-23", "città_nascita": "Freiberg", "città_morte": "Londra"},
    {"nome": "Carl Jung", "nascita": "1875-07-26", "morte": "1961-06-06", "città_nascita": "Kesswil", "città_morte": "Küsnacht"},
    
  

    # 100 nuovi personaggi famosi aggiunti
    # Filosofi e pensatori
    {"nome": "Socrate", "nascita": "-0469-01-01", "morte": "-0399-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Platone", "nascita": "-0427-01-01", "morte": "-0347-01-01", "città_nascita": "Atene", "città_morte": "Atene"},
    {"nome": "Aristotele", "nascita": "-0384-01-01", "morte": "-0322-01-01", "città_nascita": "Stagira", "città_morte": "Calcide"},
    {"nome": "Confucio", "nascita": "-0551-09-28", "morte": "-0479-04-11", "città_nascita": "Qufu", "città_morte": "Qufu"},
    {"nome": "Immanuel Kant", "nascita": "1724-04-22", "morte": "1804-02-12", "città_nascita": "Königsberg", "città_morte": "Königsberg"},
    {"nome": "Friedrich Nietzsche", "nascita": "1844-10-15", "morte": "1900-08-25", "città_nascita": "Röcken", "città_morte": "Weimar"},
    {"nome": "Jean-Jacques Rousseau", "nascita": "1712-06-28", "morte": "1778-07-02", "città_nascita": "Ginevra", "città_morte": "Ermenonville"},
    {"nome": "René Descartes", "nascita": "1596-03-31", "morte": "1650-02-11", "città_nascita": "La Haye en Touraine", "città_morte": "Stoccolma"},

    # Scienziati e inventori
    {"nome": "Thomas Edison", "nascita": "1847-02-11", "morte": "1931-10-18", "città_nascita": "Milan", "città_morte": "West Orange"},
    {"nome": "Alexander Graham Bell", "nascita": "1847-03-03", "morte": "1922-08-02", "città_nascita": "Edimburgo", "città_morte": "Beinn Bhreagh"},
    {"nome": "Enrico Fermi", "nascita": "1901-09-29", "morte": "1954-11-28", "città_nascita": "Roma", "città_morte": "Chicago"},
    {"nome": "Guglielmo Marconi", "nascita": "1874-04-25", "morte": "1937-07-20", "città_nascita": "Bologna", "città_morte": "Roma"},
    {"nome": "Louis Pasteur", "nascita": "1822-12-27", "morte": "1895-09-28", "città_nascita": "Dole", "città_morte": "Marnes-la-Coquette"},
    {"nome": "Antoine Lavoisier", "nascita": "1743-08-26", "morte": "1794-05-08", "città_nascita": "Parigi", "città_morte": "Parigi"},
    {"nome": "Rachel Carson", "nascita": "1907-05-27", "morte": "1964-04-14", "città_nascita": "Springdale", "città_morte": "Silver Spring"},
    {"nome": "Max Planck", "nascita": "1858-04-23", "morte": "1947-10-04", "città_nascita": "Kiel", "città_morte": "Göttingen"},
    {"nome": "Lise Meitner", "nascita": "1878-11-07", "morte": "1968-10-27", "città_nascita": "Vienna", "città_morte": "Cambridge"},
    {"nome": "Richard Feynman", "nascita": "1918-05-11", "morte": "1988-02-15", "città_nascita": "New York", "città_morte": "Los Angeles"},

    # Artisti e scrittori
    {"nome": "William Shakespeare", "nascita": "1564-04-26", "morte": "1616-04-23", "città_nascita": "Stratford-upon-Avon", "città_morte": "Stratford-upon-Avon"},
    {"nome": "Michelangelo", "nascita": "1475-03-06", "morte": "1564-02-18", "città_nascita": "Caprese", "città_morte": "Roma"},
    {"nome": "Vincent van Gogh", "nascita": "1853-03-30", "morte": "1890-07-29", "città_nascita": "Zundert", "città_morte": "Auvers-sur-Oise"},
    {"nome": "Pablo Picasso", "nascita": "1881-10-25", "morte": "1973-04-08", "città_nascita": "Málaga", "città_morte": "Mougins"},
    {"nome": "Johann Wolfgang von Goethe", "nascita": "1749-08-28", "morte": "1832-03-22", "città_nascita": "Francoforte", "città_morte": "Weimar"},
    {"nome": "Virginia Woolf", "nascita": "1882-01-25", "morte": "1941-03-28", "città_nascita": "Londra", "città_morte": "Lewes"},
    {"nome": "Frida Kahlo", "nascita": "1907-07-06", "morte": "1954-07-13", "città_nascita": "Coyoacán", "città_morte": "Coyoacán"},
    {"nome": "Claude Monet", "nascita": "1840-11-14", "morte": "1926-12-05", "città_nascita": "Parigi", "città_morte": "Giverny"},
    {"nome": "Marcel Proust", "nascita": "1871-07-10", "morte": "1922-11-18", "città_nascita": "Auteuil", "città_morte": "Parigi"},
    {"nome": "Jane Austen", "nascita": "1775-12-16", "morte": "1817-07-18", "città_nascita": "Steventon", "città_morte": "Winchester"},
    {"nome": "Edgar Allan Poe", "nascita": "1809-01-19", "morte": "1849-10-07", "città_nascita": "Boston", "città_morte": "Baltimora"},
    {"nome": "Oscar Wilde", "nascita": "1854-10-16", "morte": "1900-11-30", "città_nascita": "Dublino", "città_morte": "Parigi"},

    # Personaggi politici e leader
    {"nome": "Mahatma Gandhi", "nascita": "1869-10-02", "morte": "1948-01-30", "città_nascita": "Porbandar", "città_morte": "Nuova Delhi"},
    {"nome": "Nelson Mandela", "nascita": "1918-07-18", "morte": "2013-12-05", "città_nascita": "Mvezo", "città_morte": "Johannesburg"},
    {"nome": "Abraham Lincoln", "nascita": "1809-02-12", "morte": "1865-04-15", "città_nascita": "Hodgenville", "città_morte": "Washington D.C."},
    {"nome": "Winston Churchill", "nascita": "1874-11-30", "morte": "1965-01-24", "città_nascita": "Woodstock", "città_morte": "Londra"},
    {"nome": "Giovanna d'Arco", "nascita": "1412-01-06", "morte": "1431-05-30", "città_nascita": "Domrémy", "città_morte": "Rouen"},
    {"nome": "Cleopatra", "nascita": "-0069-01-01", "morte": "-0030-08-01", "città_nascita": "Alessandria", "città_morte": "Alessandria"},
    {"nome": "Martin Luther King Jr.", "nascita": "1929-01-15", "morte": "1968-04-04", "città_nascita": "Atlanta", "città_morte": "Memphis"},
    {"nome": "Catherine de' Medici", "nascita": "1519-04-13", "morte": "1589-01-05", "città_nascita": "Firenze", "città_morte": "Blois"},
    {"nome": "Simón Bolívar", "nascita": "1783-07-24", "morte": "1830-12-17", "città_nascita": "Caracas", "città_morte": "Santa Marta"},
    {"nome": "Catherine the Great", "nascita": "1729-05-02", "morte": "1796-11-17", "città_nascita": "Stettino", "città_morte": "San Pietroburgo"},

    # Musicisti
    {"nome": "Ludwig van Beethoven", "nascita": "1770-12-17", "morte": "1827-03-26", "città_nascita": "Bonn", "città_morte": "Vienna"},
    {"nome": "Wolfgang Amadeus Mozart", "nascita": "1756-01-27", "morte": "1791-12-05", "città_nascita": "Salisburgo", "città_morte": "Vienna"},
    {"nome": "Johann Sebastian Bach", "nascita": "1685-03-31", "morte": "1750-07-28", "città_nascita": "Eisenach", "città_morte": "Lipsia"},
    {"nome": "Frédéric Chopin", "nascita": "1810-03-01", "morte": "1849-10-17", "città_nascita": "Żelazowa Wola", "città_morte": "Parigi"},
    {"nome": "Louis Armstrong", "nascita": "1901-08-04", "morte": "1971-07-06", "città_nascita": "New Orleans", "città_morte": "New York"},
    {"nome": "Elvis Presley", "nascita": "1935-01-08", "morte": "1977-08-16", "città_nascita": "Tupelo", "città_morte": "Memphis"},
    {"nome": "Ella Fitzgerald", "nascita": "1917-04-25", "morte": "1996-06-15", "città_nascita": "Newport News", "città_morte": "Beverly Hills"},
    {"nome": "Bob Marley", "nascita": "1945-02-06", "morte": "1981-05-11", "città_nascita": "Nine Mile", "città_morte": "Miami"},
    {"nome": "Maria Callas", "nascita": "1923-12-02", "morte": "1977-09-16", "città_nascita": "New York", "città_morte": "Parigi"},
    {"nome": "Giuseppe Verdi", "nascita": "1813-10-10", "morte": "1901-01-27", "città_nascita": "Roncole", "città_morte": "Milano"},

    # Altri imperatori romani
    {"nome": "Giulio Cesare", "nascita": "-0100-07-12", "morte": "-0044-03-15", "città_nascita": "Roma", "città_morte": "Roma"},
    {"nome": "Marco Aurelio", "nascita": "0121-04-26", "morte": "0180-03-17", "città_nascita": "Roma", "città_morte": "Vindobona"},
    {"nome": "Adriano", "nascita": "0076-01-24", "morte": "0138-07-10", "città_nascita": "Italica", "città_morte": "Baia"},
    {"nome": "Costantino", "nascita": "0272-02-27", "morte": "0337-05-22", "città_nascita": "Naissus", "città_morte": "Nicomedia"},
    {"nome": "Diocleziano", "nascita": "0244-12-22", "morte": "0311-12-03", "città_nascita": "Salona", "città_morte": "Spalato"},

    # Altri esploratori e navigatori
    {"nome": "Cristoforo Colombo", "nascita": "1451-10-31", "morte": "1506-05-20", "città_nascita": "Genova", "città_morte": "Valladolid"},
    {"nome": "Marco Polo", "nascita": "1254-09-15", "morte": "1324-01-08", "città_nascita": "Venezia", "città_morte": "Venezia"},
    {"nome": "Vasco da Gama", "nascita": "1469-01-01", "morte": "1524-12-24", "città_nascita": "Sines", "città_morte": "Cochin"},
    {"nome": "Ferdinando Magellano", "nascita": "1480-02-03", "morte": "1521-04-27", "città_nascita": "Sabrosa", "città_morte": "Mactan"},
    {"nome": "James Cook", "nascita": "1728-11-07", "morte": "1779-02-14", "città_nascita": "Marton", "città_morte": "Kealakekua Bay"},
    {"nome": "Amerigo Vespucci", "nascita": "1454-03-09", "morte": "1512-02-22", "città_nascita": "Firenze", "città_morte": "Siviglia"},
    {"nome": "Roald Amundsen", "nascita": "1872-07-16", "morte": "1928-06-18", "città_nascita": "Borge", "città_morte": "Mare di Barents"},
    {"nome": "Ibn Battuta", "nascita": "1304-02-25", "morte": "1369-01-01", "città_nascita": "Tangeri", "città_morte": "Marrakech"},

    # Scienziati e inventori moderni
    {"nome": "Rosalind Franklin", "nascita": "1920-07-25", "morte": "1958-04-16", "città_nascita": "Londra", "città_morte": "Londra"},
    {"nome": "Alexander Fleming", "nascita": "1881-08-06", "morte": "1955-03-11", "città_nascita": "Ayrshire", "città_morte": "Londra"},
    {"nome": "James Watt", "nascita": "1736-01-19", "morte": "1819-08-25", "città_nascita": "Greenock", "città_morte": "Handsworth"},
    {"nome": "Annie Jump Cannon", "nascita": "1863-12-11", "morte": "1941-04-13", "città_nascita": "Dover", "città_morte": "Cambridge"},
    {"nome": "Carl Sagan", "nascita": "1934-11-09", "morte": "1996-12-20", "città_nascita": "Brooklyn", "città_morte": "Seattle"},
    {"nome": "John von Neumann", "nascita": "1903-12-28", "morte": "1957-02-08", "città_nascita": "Budapest", "città_morte": "Washington D.C."},
    {"nome": "Grace Hopper", "nascita": "1906-12-09", "morte": "1992-01-01", "città_nascita": "New York", "città_morte": "Arlington"},
    {"nome": "James Clerk Maxwell", "nascita": "1831-06-13", "morte": "1879-11-05", "città_nascita": "Edimburgo", "città_morte": "Cambridge"},
    {"nome": "Marie-Anne Lavoisier", "nascita": "1758-01-20", "morte": "1836-02-10", "città_nascita": "Parigi", "città_morte": "Parigi"},
    {"nome": "Emmy Noether", "nascita": "1882-03-23", "morte": "1935-04-14", "città_nascita": "Erlangen", "città_morte": "Bryn Mawr"},
    {"nome": "Barbara McClintock", "nascita": "1902-06-16", "morte": "1992-09-02", "città_nascita": "Hartford", "città_morte": "Huntington"},
    {"nome": "Edwin Hubble", "nascita": "1889-11-20", "morte": "1953-09-28", "città_nascita": "Marshfield", "città_morte": "San Marino"},

    # Altri personaggi storici importanti
    {"nome": "Archimede", "nascita": "-0287-01-01", "morte": "-0212-01-01", "città_nascita": "Siracusa", "città_morte": "Siracusa"},
    {"nome": "Ippocrate", "nascita": "-0460-01-01", "morte": "-0370-01-01", "città_nascita": "Kos", "città_morte": "Larissa"},
    {"nome": "Pitagora", "nascita": "-0570-01-01", "morte": "-0495-01-01", "città_nascita": "Samo", "città_morte": "Metaponto"},
    {"nome": "Ibn Sina (Avicenna)", "nascita": "0980-08-23", "morte": "1037-06-21", "città_nascita": "Afshona", "città_morte": "Hamadan"},
    {"nome": "Ibn al-Haytham", "nascita": "0965-07-01", "morte": "1040-03-06", "città_nascita": "Bassora", "città_morte": "Il Cairo"},
    {"nome": "Al-Khwarizmi", "nascita": "0780-01-01", "morte": "0850-01-01", "città_nascita": "Corasmia", "città_morte": "Baghdad"},
    {"nome": "Sun Tzu", "nascita": "-0544-01-01", "morte": "-0496-01-01", "città_nascita": "Qi", "città_morte": "Wu"},
    {"nome": "Gutenberg", "nascita": "1400-01-01", "morte": "1468-02-03", "città_nascita": "Magonza", "città_morte": "Magonza"},

    # Pionieri dell'aviazione e dello spazio
    {"nome": "Fratelli Wright", "nascita": "1871-08-19", "morte": "1948-01-30", "città_nascita": "Millville", "città_morte": "Dayton"},
    {"nome": "Amelia Earhart", "nascita": "1897-07-24", "morte": "1937-07-02", "città_nascita": "Atchison", "città_morte": "Oceano Pacifico"},
    {"nome": "Jurij Gagarin", "nascita": "1934-03-09", "morte": "1968-03-27", "città_nascita": "Klušino", "città_morte": "Novosëlovo"},
    {"nome": "Neil Armstrong", "nascita": "1930-08-05", "morte": "2012-08-25", "città_nascita": "Wapakoneta", "città_morte": "Cincinnati"},
    {"nome": "Valentina Tereškova", "nascita": "1937-03-06", "morte": "2125-01-01", "città_nascita": "Maslennikovo", "città_morte": "-"},

    # Altri personaggi moderni di vari campi
    {"nome": "Charlie Chaplin", "nascita": "1889-04-16", "morte": "1977-12-25", "città_nascita": "Londra", "città_morte": "Corsier-sur-Vevey"},
    {"nome": "Walt Disney", "nascita": "1901-12-05", "morte": "1966-12-15", "città_nascita": "Chicago", "città_morte": "Burbank"}
]

# Funzione per convertire le date in formato datetime
def converti_data(data):
    try:
        return datetime.strptime(data, '%Y-%m-%d')
    except ValueError:
        if data.startswith('-'):
            return datetime.strptime(data[1:], '%Y-%m-%d').replace(year=-int(data[1:5]))
        else:
            return datetime.strptime(data, '%Y-%m-%d')

# Creazione del DataFrame
df = pd.DataFrame(personaggi)

# Conversione delle date in formato datetime usando la funzione personalizzata
df['nascita'] = df['nascita'].apply(converti_data)
df['morte'] = df['morte'].apply(converti_data)

# Creazione del diagramma di Gantt
fig, ax = plt.subplots(figsize=(14, 10))

for i, personaggio in df.iterrows():
    ax.barh(personaggio['nome'], (personaggio['morte'] - personaggio['nascita']).days, left=personaggio['nascita'])
    ax.text(personaggio['nascita'], i, personaggio['città_nascita'], va='center', ha='right', color='blue', fontsize=8)
    ax.text(personaggio['morte'], i, personaggio['città_morte'], va='center', ha='left', color='red', fontsize=8)

# Impostazione delle etichette e del titolo
ax.set_xlabel('Anno')
ax.set_ylabel('Personaggi famosi')
ax.set_title('Diagramma di Gantt: Nascita e Morte di Personaggi Famosi')

# Formattazione delle date sull'asse x
ax.xaxis_date()

plt.show()
