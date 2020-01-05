#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict


# In[35]:


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self, u, v, w): 
        self.graph.append([u,v,w])
        
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        
        f = float("inf")
        alldot = [i for i in range(0, len(self.graph))] #所有點
        new = [] #建立新的路
        
        if s in alldot:
            new.append(s)
            alldot.remove(s)
            
        way = [f]*self.V #初始路徑無限
        
        for j in range(0, len(self.graph[s])):
            if self.graph[s][j] != 0: #可到達
                way[j] = self.graph[s][j] #起點到下一點距離
                
        way[s] = 0 #起點
        
        while alldot:
            
            def mway(way):
                m = f
                for a in alldot:
                    if way[a] < m:
                        m = way[a]
                        dot1 = a
                return dot1
        
            dot = mway(way) #最近節點
        
            for a in alldot: #比較距離，較小則取代
                if  self.graph[dot][a] != 0 and (way[dot] + self.graph[dot][a] < way[a]):
                    way[a] = way[dot] + self.graph[dot][a]
            
            new.append(dot)
            alldot.remove(dot)

            out = {}
            for x in range(0,self.V):
                out[str(x)]= way[x]
                
        return out
            
    def Kruskal(self):
         """
        :rtype: dict
        """


# In[36]:


#g =Graph(4)
#g.addEdge(0, 1, 10)
#g.addEdge(0, 2, 6)
#g.addEdge(0, 3, 5)
#g.addEdge(1, 3, 15)
#g.addEdge(2, 3, 4)
#print(g)


# In[37]:


#g = Graph(9)
#g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
#           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
#           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
#           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
#           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
#           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
#           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
#           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
#           [0, 0, 2, 0, 0, 0, 6, 7, 0]];
#print("Dijkstra",g.Dijkstra(0))

#g =Graph(4)
#g.addEdge(0, 1, 10)
#g.addEdge(0, 2, 6)
#g.addEdge(0, 3, 5)
#g.addEdge(1, 3, 15)
#g.addEdge(2, 3, 4)
#print("Kruskal",g.Kruskal())


# In[ ]:




