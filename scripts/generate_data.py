import csv
import random
import math
import subprocess

def generate_csv(filename="data.csv", num_points=1000, dimensions=2, clusters=3):
    # Generar centros más cercanos (menor distancia entre ellos)
    centers = []
    min_distance = 3  # antes era 10
    max_range = 20    # reducir el rango general

    attempts = 0
    while len(centers) < clusters and attempts < 1000:
        candidate = [random.uniform(0, max_range) for _ in range(dimensions)]
        if all(math.dist(candidate, c) > min_distance for c in centers):
            centers.append(candidate)
        attempts += 1

    if len(centers) < clusters:
        raise ValueError("No se pudieron generar centros suficientemente cercanos.")

    # Aumentamos la desviación estándar para hacer que los puntos estén más dispersos
    std_dev = 8  # antes era 5 o 6

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_points):
            center = random.choice(centers)
            point = [round(random.gauss(c, std_dev), 2) for c in center]
            writer.writerow(point)

    print(f"[✓] Generado archivo '{filename}' con {num_points} puntos.")
    print(f"[INFO] Centros utilizados (más cercanos): {centers}")

def pick_initial_centers(data_file="data.csv", centers_file="centers.csv", k=3):
    with open(data_file) as f:
        data = [list(map(float, row)) for row in csv.reader(f)]

    centers = random.sample(data, k)
    print(f"[✓] Centros iniciales seleccionados: {centers}")

    with open(centers_file, 'w') as f:
        for center in centers:
            f.write(','.join(map(str, center)) + '\n')

    print(f"[✓] Generado archivo '{centers_file}' con {k} centros aleatorios.")

def upload_to_hdfs(local_file="data.csv", hdfs_path="/user/hadoop/input/data.csv"):
    subprocess.run(["hadoop", "fs", "-rm", "-f", hdfs_path], check=False)
    subprocess.run(["hadoop", "fs", "-mkdir", "-p", "/user/hadoop/input"], check=False)
    subprocess.run(["hadoop", "fs", "-put", local_file, hdfs_path])
    print(f"[✓] Subido '{local_file}' a HDFS en '{hdfs_path}'.")

if __name__ == "__main__":
    generate_csv()
    pick_initial_centers()
    upload_to_hdfs()
