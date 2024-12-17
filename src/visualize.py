import matplotlib.pyplot as plt

def plot_results(time, latency, packet_size, labels):
    # Latencija sa K-means klasterima
    plt.figure(figsize=(10, 5))
    plt.scatter(time, latency, c=labels, cmap='viridis')
    plt.axvline(x=30, color='r', linestyle='--', label="Početak napada")
    plt.axvline(x=50, color='r', linestyle='--', label="Kraj napada")
    plt.title("K-means Klasteriranje: Normalni promet vs DDoS napad")
    plt.xlabel("Vrijeme (sekunde)")
    plt.ylabel("Latencija (ms)")
    plt.legend()
    plt.show()
