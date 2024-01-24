from Algorithme.Dijkstra.summit import Summit


class Graph:
    def __init__(self, summit: [Summit]):
        self.summit = summit

    def countSummit(self):
        return len(self.summit)

    def dijkstra(self, summit1: Summit, summit2: Summit):

        for i in range(self.countSummit()):
            return min(summit1.distances.items())


summitA = Summit('A', {"A" : 0, "B" : 85, "C" : 217, "E" : 173})
summitB = Summit('B', {"A" : 85, "B" : 0, "F" : 80})
summitC = Summit('C', {"A" : 217, "C" : 0, "G" : 186, "H" : 103})
summitD = Summit('D', {"D" : 0, "H": 183})
summitE = Summit('E', {"A" : 173, "E" : 0, "J" : 502})
summitF = Summit('F', {"B" : 80, "F" : 0, "I" : 250})
summitG = Summit('G', {"C" : 186, "G" : 0})
summitH = Summit('H', {"C" : 103, "D" : 183, "H" : 0, "J": 167})
summitI = Summit('I', {"F" : 250, "I" : 0, "J" : 84})
summitJ = Summit('J', {"E" : 502, "H" : 167, "I" : 84, "J" : 0})

listSummit = [summitA, summitB, summitC, summitD, summitE, summitF, summitG, summitH, summitI, summitJ]

g = Graph(listSummit)
print(g.dijkstra(summitA, summitB))
