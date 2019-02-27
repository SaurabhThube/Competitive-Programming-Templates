def comb(n,k):
    count=1
    if k>n-k:
        k=n-k
    for j in xrange(1,k+1):
        if n%j==0:
            count*=n/j
        elif count%j==0:
            count=count/j*n
        else:
            count=(count*n)/j
        n-=1
    return count

def comb2(n,k):
    count=n
    r=2
    if k==0:
        return 1
    for i in xrange(k-1):
        count=int(((n-r+1)/(r*1.0))*count)
        r+=1
    return count


print comb(10,8)
