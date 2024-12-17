# Uvoz potrebnih biblioteka
from sklearn.cluster import KMeans  # Importuje KMeans algoritam iz biblioteke scikit-learn koji je koristi za grupisanje podataka (klasterizaciju)
import numpy as np  # Importuje numpy biblioteku koja omogućava rad sa numeričkim podacima i nizovima

def detect_ddos(latency, packet_size):
    # Kombinacija podataka u jedan niz
    data = np.column_stack((latency, packet_size))  # Kombinuje podatke o latenciji i veličini paketa u jedan 2D niz
    # 'np.column_stack' se koristi za spajanje dva niza (latency i packet_size) u jedan. Rezultat je matrica sa dvije kolone,
    # gdje je prva kolona latencija, a druga veličina paketa. Svaka red predstavlja jedan paket

    # K-Means klasterizacija
    kmeans = KMeans(n_clusters=2, random_state=0).fit(data)  # Inicijalizuje KMeans algoritam sa 2 klastera (normalno stanje i napad)
    # 'n_clusters=2' označava da želimo podijeliti podatke u dva klastera: jedan koji predstavlja normalan saobraćaj,
    # i drugi koji predstavlja napad. 'random_state=0' postavlja inicijalno stanje generatora slučajnih brojeva, što osigurava
    # ponavljanje rezultata

    labels = kmeans.labels_  # Nakon treniranja modela, dobijamo oznake klastera (labels), koje pokazuju kojoj grupi (klasteru) svaki podatak pripada
    # Ove oznake će biti 0 ili 1, gdje 0 označava jedan klaster (npr. normalan saobraćaj), a 1 označava drugi klaster (npr. napad)

    return labels  # Vraća oznake klastera (labels), koje koriste detekciju napada (0 ili 1 za svaki podatak)
