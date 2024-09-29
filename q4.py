import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key, vertex):
        heapq.heappush(self.heap, (key, vertex))

    def extract_min(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

def prim_mst(graph):
    n = len(graph)
    key = [float('inf')] * n  
    parent = [-1] * n         
    in_mst = [False] * n      

    key[0] = 0
    min_heap = MinHeap()
    min_heap.insert(0, 0)  

    while not min_heap.is_empty():
        key_value, u = min_heap.extract_min()
        in_mst[u] = True  

        
        for v, weight in graph[u]:
            if not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                min_heap.insert(key[v], v)

    print("Edge \tWeight")
    for i in range(1, n):
        print(f"{parent[i]} - {i} \t{key[i]}")

if __name__ == "__main__":
    graph = [
        [(1, 2), (3, 6)],          
        [(0, 2), (2, 3), (3, 8), (4, 5)],  
        [(1, 3), (4, 7)],          
        [(0, 6), (1, 8), (4, 9)],  
        [(1, 5), (2, 7), (3, 9)]   
    ]

    prim_mst(graph)
