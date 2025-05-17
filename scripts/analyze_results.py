import matplotlib.pyplot as plt
import csv
import os

def load_data(data_file):
    with open(data_file) as f:
        return [list(map(float, row)) for row in csv.reader(f)]

def load_centers(center_file):
    centers = []
    with open(center_file) as f:
        for line in f:
            parts = line.strip().split(':')
            if len(parts) == 2:
                center = eval(parts[1])
                centers.append(center)
    return centers

def plot_clusters(data, centers, filename, title="Resultados KMeans"):
    xs, ys = zip(*data)
    cx, cy = zip(*centers)

    plt.figure(figsize=(8, 6))
    plt.scatter(xs, ys, alpha=0.4, label='Datos')
    plt.scatter(cx, cy, color='red', marker='x', s=100, label='Centros')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    os.makedirs('plots', exist_ok=True)
    data = load_data("data.csv")

    for i in range(10):  # cambia si haces más/menos iteraciones
        file = f"results/output_iter_{i}.txt"
        if os.path.exists(file):
            centers = load_centers(file)
            plot_clusters(data, centers, f"plots/iter_{i}.png", f"Iteración {i}")
            print(f"[✓] Gráfico guardado: plots/iter_{i}.png")

    print("✅ Análisis completo. Ver carpeta 'plots'.")
