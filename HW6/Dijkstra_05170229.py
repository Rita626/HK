from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = defaultdict(list) 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph[u].append(v)
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
    def Kruskal(self):
        """
        :rtype: dict
        """
