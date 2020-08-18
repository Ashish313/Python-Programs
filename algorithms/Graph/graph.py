
class Graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    # add new vertex
    def addVertex(self,vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx]=[]
        else:
            print(f"vertex '{vrtx}' is already present.\n")

    # list all the vertices present
    def showVertex(self):
        return list(self.gdict.keys())

    # add an edge
    def addEdge(self,edge):
        edge=set(edge)
        vrtx1,vrtx2=tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1]=[vrtx2]

    # list all the edges present
    def showEdge(self):
        edgename=[]
        for vrtx in self.gdict:
            for next_vrtx in self.gdict[vrtx]:
                if {vrtx,next_vrtx} not in edgename:
                    edgename.append({vrtx,next_vrtx})

        return edgename


# create the graph
graph={'a':['b','c'], 'b':['a','d'], 'c':['a','d'],'d':['e'],'e':['d']}
g=Graph(graph)

g.addVertex('e')
g.addVertex('f')

print(f"Vertices: {', '.join(g.showVertex())}\n")

g.addEdge({'a','e'})
g.addEdge({'a','c'})

print(f'Edges: {g.showEdge()}\n')



