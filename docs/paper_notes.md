# Paper Notes

## Título: "Parallel K-Means Clustering Based on MapReduce"

- `Parallel`: A primera vista se podría asumir que se ejecuta en varios (procesadores/computadores) al mismo tiempo.
- `K-Means Clustering`: Es un algoritmo. Por ejemplo, 1,000 puntos de colores diferentes y organizarlos automáticamente en 3 grupos: K-Means puede hacerlo.
- `Based on MapReduce`: Se usa MapReduce para dividir y distribuir el trabajo.

> En palabras simples, proponen una forma de hacer K-Means más rápido y escalable usando MapReduce.

---

## Abstract

- Clustering es importante en campos como:
  - minería de datos (encontrar patrones),
  - recuperación de documentos (como Google busca documentos),
  - segmentación de imágenes (dividir una imagen en partes), y
  - clasificación de patrones (como reconocer letras o caras).

Se necesita organizar datos sin supervisión.

- La cantidad de datos en el mundo está creciendo muchísimo (como fotos, textos, sensores). Eso hace que usar métodos normales para agrupar datos se vuelva muy difícil y lento.

- Para resolver ese problema, se busca formas de hacer algoritmos más rápidos usando paralelismo.

- Proponen en este articulo una versión del algoritmo K-Means con paralelismo, usando MapReduce.

Hicieron pruebas y vieron que su propuesta funciona bien incluso con datos grandes, y sin necesidad de computadores especiales, solo con hardware común (como PCs o VMs normales).

---

## Keywords

- `Data mining`: Analizar datos para descubrir patrones.
- `Parallel clustering`: Agrupar datos en paralelo.
- `K-means`: El algoritmo usado.
- `Hadoop`: Una plataforma donde se puede usar MapReduce para trabajar con datos distribuidos.
- `MapReduce`: Técnica distribuida que divide el trabajo en dos fases: mapear (repartir tareas) y reducir (juntar resultados).

---

## 1. Introducción

- El problema de escalar clustering
  - La cantidad de datos que procesan las aplicaciones es enorme, superando incluso los petabytes.
  - Se necesita mucho poder para procesar y analizar esos datos.
  - Para manejar ese volumen de datos, se necesita algoritmos de clustering paralelos, que sean eficientes (rápidos y con buen uso de recursos).
  - También, se necesita técnicas de implementación (cómo se programan y ejecutan) que sean escalables (funcionen bien incluso si los datos crecen mucho).

- Las limitaciones de algoritmos anteriores
  - Los algoritmos anteriores tienen dos grandes problemas:
    - Suponen que todos los datos caben en memoria RAM al mismo tiempo.
    - Modelos de programación muy limitados que no permiten mucha flexibilidad, sino que imponen reglas que intentan paralelizar automáticamente, pero con restricciones.
  - Estas dos suposiciones hacen que esos algoritmos no funcionen bien con datos muy grandes.

En este articulo proponen que se diseñen algoritmos paralelos que estén orientados a los datos (es decir, que se adapten al tamaño y estructura de los datos, y no dependan de suposiciones irreales).

- Introducción a MapReduce
  - MapReduce es una forma de programar para procesar grandes volúmenes de datos.
  - Funciona bien en muchas tareas del mundo real, no solo en clustering.
  - Solo senecesitarian definir dos cosas:
    - Una función map: divide el trabajo (por ejemplo, cada máquina agrupa sus propios datos).
    - Una función reduce: junta los resultados (por ejemplo, sumar los centros de los grupos de todas las máquinas).
  - MapReduce se encarga del resto: distribuye el trabajo, maneja fallos (si una máquina se cae), y usa bien la red y los discos para mover y guardar la información.
  - Google inventó MapReduce, y Hadoop.

- Qué hacen en este paper
  - Adaptan K-Means para que funcione dentro de Hadoop usando MapReduce.
  - Permitiendo aplicarlo a datos de gran escala.
  - En MapReduce, todo se basa en pares clave-valor (como en un diccionario).
    - Una clave puede ser el número de cluster, y los valores los puntos asignados a ese cluster.

---

## 2. Parallel K-Means Algorithm Based on MapReduce
