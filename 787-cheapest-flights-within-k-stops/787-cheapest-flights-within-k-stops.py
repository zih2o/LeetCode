class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u,v,w in flights:
            graph[u].append((v,w))
        
        visit = {}
        
        Q = [(0, src, K)]
        
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst and k >= -1:
                return price
            if node not in visit or k > visit[node]:
                visit[node] = k
                for v,w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1