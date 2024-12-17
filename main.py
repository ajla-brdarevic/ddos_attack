# Uvoz funkcija iz drugih modula
from src.simulate_data import generate_data  # Funkcija koja generira podatke (latenciju, veličinu paketa, vrijeme)
from src.kmeans_detection import detect_ddos  # Funkcija koja koristi K-means za detekciju DDoS napada
from src.visualize import plot_results  # Funkcija za vizualizaciju rezultata detekcije

def main():
    # Generiranje podataka koji će se koristiti u analizi
    # Poziva se funkcija 'generate_data' koja generira simulirane podatke sa tri parametra:
    # - 'time': Vremenski podaci (vrijeme kada je saobraćaj došao)
    # - 'latency': Latencija, tj. kašnjenje paketa u mreži (vrijednost koja može varirati tokom napada)
    # - 'packet_size': Veličina paketa koji se šalje u mrežu (može biti pokazatelj ponašanja saobraćaja tokom napada)
    time, latency, packet_size = generate_data()

    # Primjena K-means algoritma za detekciju DDoS napada
    # Funkcija 'detect_ddos' koristi K-means algoritam za analizu latencije i veličine paketa
    # 'latency' i 'packet_size' predstavljaju ulazne podatke, dok funkcija vraća 'labels' koji označavaju
    # klasifikaciju saobraćaja (0 za normalni saobraćaj, 1 za napad)
    labels = detect_ddos(latency, packet_size)

    # Vizualizacija rezultata
    # Funkcija 'plot_results' koristi podatke za vizualizaciju saobraćaja i oznake za napad
    # 'time' predstavlja vrijeme dolaska paketa, dok 'latency' i 'packet_size' predstavljaju odgovarajuće
    # karakteristike paketa. 'labels' sadrži informacije o tome koji su paketi klasifikovani kao napad
    plot_results(time, latency, packet_size, labels)

if __name__ == "__main__":
    main()  # Poziva glavnu funkciju 'main' kada se skripta pokrene
