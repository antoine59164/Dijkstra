from Algorithme.Dijkstra.summit import Summit
from Algorithme.Dijkstra.utils import *


class Graph:
    def __init__(self, summits: [Summit]):
        self.summits = summits

    def countSummit(self):
        return len(self.summits)

    def arrayOfValue(self):
        result = []
        for i in range(self.countSummit()):
            for j, value in self.summits[i].distances.items():
                result.append(value)
        return result

    def dijkstra(self, startedSummit: Summit):

        summitProgress = startedSummit
        summitsRemaining = self.summits
        summitsTreaty = []

        while len(summitsRemaining) != 0:
            nameMinSummit = summitProgress.mindistances()[0]
            for x in summitsRemaining:
                if x.name == nameMinSummit:
                    summitsRemaining.remove(x)
                    summitsTreaty.append(x)
                    summitProgress = x


summitA = Summit('A', {"A": 0, "B": 85, "C": 217, "D": None, "E": 173, "F": None, "G": None, "H": None, "I": None,
                       "J": None})
summitB = Summit('B', {"A": 85, "B": 0, "C": None, "D": None, "E": None, "F": 80, "G": None, "H": None, "I": None,
                       "J": None})
summitC = Summit('C', {"A": 217, "B": None, "C": 0, "D": None, "E": None, "F": None, "G": 186, "H": 103, "I": None,
                       "J": None})
summitD = Summit('D', {"A": None, "B": None, "C": None, "D": 0, "E": None, "F": None, "G": None, "H": 183, "I": None,
                       "J": None})
summitE = Summit('E', {"A": 173, "B": None, "C": None, "D": None, "E": 0, "F": None, "G": None, "H": None, "I": None,
                       "J": 502})
summitF = Summit('F', {"A": None, "B": 80, "C": None, "D": None, "E": None, "F": 0, "G": None, "H": None, "I": 250,
                       "J": None})
summitG = Summit('G', {"A": None, "B": None, "C": 186, "D": None, "E": None, "F": None, "G": 0, "H": None, "I": None,
                       "J": None})
summitH = Summit('H', {"A": None, "B": None, "C": 103, "D": 183, "E": None, "F": None, "G": None, "H": 0, "I": None,
                       "J": 167})
summitI = Summit('I', {"A": None, "B": None, "C": None, "D": None, "E": None, "F": 250, "G": None, "H": None, "I": 0,
                       "J": 84})
summitJ = Summit('J', {"A": None, "B": None, "C": None, "D": None, "E": 502, "F": None, "G": None, "H": 167, "I": 84,
                       "J": 0})

listSummit = [summitA, summitB, summitC, summitD, summitE, summitF, summitG, summitH, summitI, summitJ]

g = Graph(listSummit)
g.dijkstra(summitA, summitB)
