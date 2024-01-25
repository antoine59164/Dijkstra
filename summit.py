class Summit:
    def __init__(self, name, distances):
        self.name = name
        self.distances = distances

    def mindistances(self):
        min = None
        for key, value in self.distances.items():
            if key != self.name and value is not None:
                if min is None or value < min:
                    min = value
        return min
