import heapq
    
N = int(input())
A,B,C=map(int,input().split())
M = min(A, B, C)
INF = 2*(10**18)
dst = [INF]*M
sr = 1%M
dst[sr] = 1
Hp = [(1, sr)]
coins = [i for i in (A, B, C) if i != M]
while Hp:
    d, u = heapq.heappop(Hp)
    if d <= dst[u]:
        for i in coins:
            v = (u + i) % M
            nd = d + i
            if nd < dst[v]:
                dst[v] = nd
                heapq.heappush(Hp, (nd, v))
                
res = 0
for d in dst:
    if d <= N:
        res += (N - d) // M + 1
print(res)
