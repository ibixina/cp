G = [
        [0, 20, 20, 0],
        [0, 0, 0, 20],
        [0, 1, 0, 20],
        [0, 0, 0, 0]
    ]

Gf = [
        [0, 20, 11, 0],
        [0, 0, 0, 20],
        [0, 1, 0, 20],
        [0, 0, 1, 8]
    ]

def printGraph(G):
    for i in range(len(G)):
        for j in range(len(G)):
            print(f"{G[i][j]}".ljust(4), end=' ')
        print()

def BFS(G, start, end):
    visited = set()
    queue = [(start, [start])]
    while queue:
        (v, path) = queue.pop(0)
        if v == end:
            return path
        visited.add(v)
        for vertex in range(len(G)):
            if G[v][vertex] > 0 and vertex not in visited:
                queue.append((vertex, path + [vertex]))
    return None
    
def InitializeFlow(G):
    # 0 flow
    RG = [[0 for i in range(len(G))] for j in range(len(G))]
    return RG

def residual(G, flow):
    RG = [[0 for i in range(len(G))] for j in range(len(G))]
    for vertex in range(len(G)):
        for neighbor in range(len(G)):
            if G[vertex][neighbor] > 0: # there is capacity
                # check residual capacity
                residual = G[vertex][neighbor] - flow[vertex][neighbor]
                RG[vertex][neighbor] = residual # push remaining capacity
                RG[neighbor][vertex] = flow[vertex][neighbor] # reverse flow
    return RG
                    
def AugmentingPath(RG):
    path = BFS(RG, 0, len(RG) - 1)
    return path

def ShortestAugmentingPath(RG):
    path = AugmentingPath(RG)
    return path

G = Gf
print("Capacity Graph")
printGraph(G)

flow = InitializeFlow(G)
print("Flow Graph")
printGraph(flow)

print("Residual Graph")
residualG = residual(G, flow)
printGraph(residualG)

path = ShortestAugmentingPath(residualG)
print("Shortest Augmenting Path")
print(" ".join([str(i) for i in path]))

