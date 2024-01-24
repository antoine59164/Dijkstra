class Summit:
    def __init__(self, name, distances):
        self.name = name
        self.distances = distances

    def mindistances(self):
        for key, value in self.distances.items():
            if key != self.name:
                if value < min:
                    min = value
        return min