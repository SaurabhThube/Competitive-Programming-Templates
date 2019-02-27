mod=10**9+7

def matrix(x,y):
    z=[[0,0],[0,0]]
    for i in xrange(2):
        for j in xrange(2):
            for k in xrange(2):
                z[i][j]=(z[i][j]+x[i][k]*y[k][j])%mod
    return z

def fast(res,b):
    c=[[0,1],[1,1]]
    while(b!=0):
        if b&1:
            res=matrix(res,c)
        c=matrix(c,c)
        b/=2
    return res

for _ in xrange(input()):
    a=map(int,raw_input().split())
    if a[2]<2:
        print a[a[2]]
    else:
        print fast([[a[0],a[1]],[0,0]],a[2]-1)[0][1]
