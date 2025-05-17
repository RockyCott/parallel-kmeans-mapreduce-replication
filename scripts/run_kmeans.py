import subprocess
import os
import ast
import argparse

def run_kmeans(
    local_input='data.csv',
    hdfs_input='hdfs:///user/hadoop/input/data.csv',
    local_centers='centers.csv',
    k=3,
    max_iter=10,
    mode='local'
):
    # Validación simple:
    if mode not in ('local', 'hadoop'):
        raise ValueError("Modo inválido. Use 'local' o 'hadoop'.")

    os.makedirs('results', exist_ok=True)

    print(f"[•] Ejecutando KMeans en modo '{mode}' con k={k}, iter={max_iter}")

    for i in range(max_iter):
        print(f"[•] Iteración {i}")

        output_file = f'results/output_iter_{i}.txt'

        cmd = [
            'python', 'pkmeans.py',
            '-r', mode,
            '--centers', local_centers
        ]

        if mode == 'local':
            cmd += ['--input', local_input]
        else:
            cmd += [hdfs_input]

        # Ejecutar y capturar salida
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print(f"[ERROR] Iteración {i} falló:\n{result.stderr}")
            break

        # Parsear nuevos centros desde la salida
        new_centers = []
        for line in result.stdout.strip().split('\n'):
            if '\t' not in line:
                continue
            key, val = line.split('\t')
            center = ast.literal_eval(val)
            new_centers.append(center)

        if len(new_centers) != k:
            print(f"[ADVERTENCIA] Se encontraron {len(new_centers)} centros, se esperaba {k}")

        # Guardar nuevos centros
        with open(local_centers, 'w') as f:
            for center in new_centers:
                f.write(','.join(map(str, center)) + '\n')

        # Guardar salida de la iteración para revisión
        with open(output_file, 'w') as f:
            for idx, center in enumerate(new_centers):
                f.write(f'{idx}: {center}\n')

        print(f"[✓] Iteración {i} completada → {output_file}")

    print("✅ KMeans terminado. Resultados en la carpeta 'results'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecuta KMeans en modo local o Hadoop.")
    parser.add_argument('--mode', choices=['local', 'hadoop'], default='local',
                        help="Modo de ejecución: 'local' o 'hadoop' (default: local)")
    parser.add_argument('--local_input', default='data.csv', help="Archivo de datos local")
    parser.add_argument('--hdfs_input', default='hdfs:///user/hadoop/input/data.csv', help="Ruta HDFS de datos")
    parser.add_argument('--centers', default='centers.csv', help="Archivo de centros local")
    parser.add_argument('-k', type=int, default=3, help="Número de clusters")
    parser.add_argument('--max_iter', type=int, default=10, help="Número máximo de iteraciones")

    args = parser.parse_args()

    run_kmeans(
        local_input=args.local_input,
        hdfs_input=args.hdfs_input,
        local_centers=args.centers,
        k=args.k,
        max_iter=args.max_iter,
        mode=args.mode
    )
