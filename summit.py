class Summit:
    def __init__(self, name, distances):
        self.name = name
        self.distances = distances



    def mindistances(self):
        min = None
        keyResult = None
        for key, value in self.distances.items():
            if key != self.name and value is not None:
                if min is None or value < min:
                    keyResult = key
                    min = value

        return keyResult, min
