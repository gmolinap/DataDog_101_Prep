"""

Dijkstra Algorithm  - Shortest Path Algorithm
You are working with the microservices architecture and you have a graph of servers.
Each server is represented with its IP address. You know the duration of sending your data
from server[i] to server[j]. As an input, you have an IP address from the starting server and the end
server and you need to find the path from the 'start' to 'end' which takes the minimum amount of time
and show its path.

1. Questions?
How many servers do we have?
How many paths do we have?
How many requests do we have?

Input: [Ip address start, Ip address final, duration/time]

2. Approach:
We should create a class to store the nodes and then create the methods to access them.
We should create a graph with the nodes and the connections between them.
"""






"""

Dijkstra Algorithm  - How long does it takes to all nodes receive a signal


1. Questions?

Approach: 
If it's impossible for all nodes to receive a signal, return -1

BFS - Breadth First Search
Minimum Heap 


"""
import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times:List[List[int]], n:int, k:int) -> int:
        edges = collections.defaultdict(list)

        # Step 1: Initialize graph, minHeap, visit set, and time variable
        #u nodo partida, v nodo llegada, w weight
        # iterar en una lista de listas
        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)] #weight, node -> we are going to start with the node k and the weight 0
        heapq.heapify(minHeap)
        print(minHeap)

        visit = set() #visited nodes
        t = 0 #time to reach all nodes
        print(edges)

        # Step 2: Implement Dijkstra's algorithm using a min-heap
        while minHeap: #while we have nodes to visit
            w1, n1 = heapq.heappop(minHeap)  #we are going to pop the node with the minimum weight
            print(w1, n1)
            print(visit)

            if n1 in visit: #if the node is already visited we
                continue
            visit.add(n1) # we are going to add the node to the visited nodes
            t = max(t, w1) # we are going to take the maximum time to reach all nodes
            print(t)

            print("Next node")
            for n2, w2 in edges[n1]: #here we are going to the next node
                print(n2, w2)
                if n2 not in visit: #if the node is not visited we are going to add it to the minHeap
                    heapq.heappush(minHeap, (w1+w2, n2)) # we are going to add the weight of the node to the minHeap
                    print(minHeap)
        # Step 3: Return the result based on whether all nodes were visited
        return t if len(visit) == n else -1


    
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

s = Solution()
print(s.networkDelayTime(times, n, k))



