def FastExpo(x,y,mod):
    res=1
    while(y>0):
        if y&1:
            res=(res*x)%mod
        x=(x*x)%mod
        y/=2
    return res
