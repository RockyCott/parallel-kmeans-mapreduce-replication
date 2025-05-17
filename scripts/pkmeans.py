import sys
import math
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRPKMeans(MRJob):
    def configure_args(self):
        super().configure_args()
        self.add_file_arg('--centers')
        self.add_passthru_arg('--input', help='Archivo de entrada local opcional')

    def load_centers(self):
        with open(self.options.centers, 'r') as f:
            self.centers = [list(map(float, line.strip().split(','))) for line in f.readlines()]

    def steps(self):
        return [MRStep(mapper_init=self.mapper_init,
                       mapper=self.mapper,
                       combiner=self.combiner,
                       reducer=self.reducer)]

    def mapper_init(self):
        self.load_centers()

    def closest_center(self, point):
        min_dist = float('inf')
        idx = -1
        for i, center in enumerate(self.centers):
            dist = math.sqrt(sum((c - p)**2 for c, p in zip(center, point)))
            if dist < min_dist:
                min_dist = dist
                idx = i
        return idx

    def mapper(self, _, line):
        point = list(map(float, line.strip().split(',')))
        idx = self.closest_center(point)
        yield idx, (point, 1)

    def combiner(self, key, values):
        total = None
        count = 0
        for val, c in values:
            if total is None:
                total = val[:]
            else:
                total = [x + y for x, y in zip(total, val)]
            count += c
        yield key, (total, count)

    def reducer(self, key, values):
        total = None
        count = 0
        for val, c in values:
            if total is None:
                total = val[:]
            else:
                total = [x + y for x, y in zip(total, val)]
            count += c
        new_center = [x / count for x in total]
        yield key, new_center


if __name__ == '__main__':
    import sys

    # Buscamos si se pasó --input y reemplazamos el argumento posicional (último arg)
    # Solo si el modo es local
    if '--input' in sys.argv:
        input_index = sys.argv.index('--input')
        if input_index + 1 < len(sys.argv):
            input_file = sys.argv[input_index + 1]
            # Removemos --input y su argumento
            sys.argv.pop(input_index)  # --input
            sys.argv.pop(input_index)  # archivo
            # Insertamos el archivo input_file como último argumento posicional
            sys.argv.append(input_file)

    MRPKMeans.run()
