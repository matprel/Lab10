import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMapTot = {}

    def buildGraph(self, anno):
        allNodi = DAO.getNazioni(anno)
        self._grafo.add_nodes_from(allNodi)
        for n in allNodi:
            self._idMapTot[n.CCode] = n

        allConfini = DAO.getConfiniAnno(anno)
        for c in allConfini:
            n1= self._idMapTot[c.state1no]
            n2 = self._idMapTot[c.state2no]
            self._grafo.add_edge(n1, n2)

    def calcolaRaggiungibili(self, stato):
        albero = nx.bfs_tree(self._grafo, stato)
        return albero


    def getNumConfinanti(self, n):
        return len(list(self._grafo.neighbors(n)))

    def getNodi(self):
        return list(self._grafo.nodes)

    def getNumConnesse(self):
        return len(list(nx.connected_components(self._grafo)))

