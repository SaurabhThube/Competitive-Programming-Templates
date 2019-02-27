def floyd():
    for k in xrange(a[0]):
        for i in xrange(a[0]):
            for j in xrange(a[0]):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[i][k]


inf = 10 ** 10
a = map(int, raw_input().split())
dist = [[inf for i in xrange(a[0])] for j in xrange(a[0])]
path = [[-1 for i in xrange(a[0])] for j in xrange(a[0])]
for i in xrange(a[1]):
    c = map(int, raw_input().split())
    dist[c[0] - 1][c[1] - 1] = c[2]
    path[c[0] - 1][c[1] - 1] = c[1] - 1
floyd()
count = dist[a[2] - 1][a[3] - 1]
#print count
if count >= inf:
    print -1
else:
    paths = [a[2] - 1]
    u = a[2] - 1
    while u!=a[3]-1:
        u = path[u][a[3] - 1]
        paths.append(u)
    paths=paths[::-1]
    #print paths
    i=0
    set = 0
    lt=len(paths)
    while (i != lt - 1):
        if dist[paths[i]][paths[i+1]] != -1:
            #print dist[paths[i]][paths[i+1]]
            count += dist[paths[i]][paths[i+1]]
        else:
            set = 1
            break
        i += 1
    if set == 0:
        print count
    else:
        print -1



