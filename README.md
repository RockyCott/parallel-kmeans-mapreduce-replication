# Parallel K-means MapReduce Replication

This repository contains an experimental implementation and replication of the algorithm presented in the paper:

**"Parallel K-means Clustering Based on MapReduce" by Zhao et al.**

## Objective

The goal of this project is to replicate and validate the results of the paper using:

- Python and the `mrjob` library (MapReduce framework)
- A custom-built 3-node virtual machine cluster
- Real or synthetic large-scale datasets (CSV format)
- Iterative control logic outside the MapReduce job

## Tools and Technologies

- Python 3.x
- [`mrjob`](https://mrjob.readthedocs.io/en/latest/) (for MapReduce jobs)
- Jupyter Notebook (for orchestration and analysis)
- SSH + Hadoop-compatible file distribution for cluster setup

## Roadmap

This project is in progress. Planned milestones include:

### Etapa 1: Lectura y Comprensión del Paper

- [x] Leer el paper y entender el algoritmo
- [ ] Identificar los pasos y componentes clave del algoritmo

### Etapa 2: Preparación del Entorno

- [ ] Create cluster and test communication
- [x] Configurar el entorno de Python y Jupyter Notebook
- [ ] Instalar dependencias necesarias (`mrjob`, `numpy`, `pandas`, etc.)

## 📄 Paper Reference

Zhao, W., Ma, H., & He, Q. (2009). *Parallel K-means Clustering Based on MapReduce*. In IEEE International Conference on Cloud Computing (CLOUD). [IEEE Xplore Link](https://doi.org/10.1109/CLOUD.2009.84)
