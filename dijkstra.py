'''
Author: Saurabh Thube

description: dijkstra algo for multiple edges between two nodes
'''

import heapq as pq
 
INF = float('inf')
 
 
def dij(g, start, end):
    h = []
    pq.heappush(h, (0, start))
    while h:
        c, i = pq.heappop(h)
 
        if i == end:
            return c
 
        for cj in g[i]:
            new_cost = cj[0] + c
            j = cj[1]
            new_cj = new_cost, j
            pq.heappush(h, new_cj)
 
    return -1


''''''
def dijkstra(x):
    sptSet=[x]
    j=0
    while(len(sptSet)!=a[0]):
        x=sptSet[j]
        for i in arr[x]:
            if dist[x]+weight[x][i]<dist[i] and Truth[i]==True:
                dist[i]=dist[x]+weight[x][i]
                income[i]=x
        Truth[x]=False
        mini=10**20
        ind=0
        for i in xrange(a[0]):
            if dist[i]<mini and Truth[i]==True:
                mini=dist[i]
                ind=i
        sptSet.append(ind)
        j+=1
    return
        
        
for _ in xrange(input()):
    a=map(int,raw_input().split())
    arr=[]
    income=[]
    Truth=[]
    dist=[]
    weight=[]
    for i in xrange(a[0]):
        arr.append([])
        weight.append([0]*(3*(10**3)))
        income.append(0)
        dist.append(10**20)
        Truth.append(True)
    for i in xrange(a[1]):
        b=map(int,raw_input().split())
        if weight[b[0]-1][b[1]-1]!=0:
            if b[2]<weight[b[0]-1][b[1]-1]:
                weight[b[0]-1][b[1]-1]=b[2]
                weight[b[1]-1][b[0]-1]=b[2]
        else:
            arr[b[0]-1].append(b[1]-1)
            arr[b[1]-1].append(b[0]-1)
            weight[b[0]-1][b[1]-1]=b[2]
            weight[b[1]-1][b[0]-1]=b[2]
    val=input()
    dist[val-1]=0
    dijkstra(val-1)
    for i in xrange(a[0]):
        if i!=val-1:
            if dist[i]==10**20:
                print -1,
            else:
                print dist[i],
    print
