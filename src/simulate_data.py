# Uvoz biblioteke za rad sa numeričkim podacima
import numpy as np  # Importovanje numpy biblioteku koja omogućava rad sa nizovima i generisanje nasumičnih podataka

def generate_data():
    # Generiranje simuliranih podataka
    time = np.arange(0, 100, 1)  # Generisanje niza brojeva od 0 do 99 (ukupno 100 vrijednosti), koji predstavljaju vrijeme
    # 'np.arange(0, 100, 1)' stvara niz brojeva od 0 do 99 sa korakom 1
    # Ovaj niz se koristi kao vremenski interval za simulirane podatke

    latency = np.random.normal(10, 2, 100)  # Generiše 100 nasumičnih vrijednosti za latenciju iz normalne distribucije sa srednjom vrijednošću 10 i standardnom devijacijom 2
    # 'np.random.normal(10, 2, 100)' stvara 100 nasumičnih brojeva koji prate normalnu (Gaussovu) distribuciju
    # Ove vrijednosti predstavljaju latenciju (kašnjenje) paketa u mreži, u ms (milisekundama)

    packet_size = np.random.normal(500, 50, 100)  # Generiše 100 nasumičnih vrijednosti za veličinu paketa iz normalne distribucije sa srednjom vrijednošću 500 i standardnom devijacijom 50
    # 'np.random.normal(500, 50, 100)' stvara 100 nasumičnih brojeva koji prate normalnu distribuciju
    # Ove vrijednosti predstavljaju veličinu paketa u bajtovima, koja je uobičajena za normalni mrežni saobraćaj

    # Simulacija DDoS napada
    latency[30:50] = np.random.normal(100, 10, 20)  # U periodu od 30. do 49. elementa (20 elemenata), postavlja latenciju na viši nivo, kako bi se simulirao napad.
    # Generiše latenciju od 100 ms sa standardnom devijacijom 10, što je daleko veće nego prethodno generisane vrijednosti latencije
    # To nam omogućava da simuliramo kašnjenje koje se može dogoditi tokom DDoS napada (napad može izazvati kašnjenje u mreži)

    packet_size[30:50] = np.random.normal(5000, 500, 20)  # U istom vremenskom periodu (30. do 49. element), postavlja veličinu paketa na znatno veću vrijednost, simulirajući DDoS napad
    # Generiše veličinu paketa od 5000 bajtova sa standardnom devijacijom 500, što je znatno veće od uobičajenih 500 bajtova
    # Ovaj korak simulira napad gdje se veličina paketa povećava uslijed napada, jer napadači često šalju pakete veće veličine kako bi preopteretili mrežu

    # Vraća generisane podatke
    return time, latency, packet_size
    # Funkcija 'generate_data' vraća tri niza: 'time', 'latency', i 'packet_size'
    # Ovi podaci će se koristiti kasnije za analizu mrežnog saobraćaja i detekciju DDoS napada
