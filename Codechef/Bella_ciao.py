def func(D,d,p,q):
    x=D//d
    return ((x)*(2*p+(x-1)*q))//2
    
t=int(input())
for _ in range(t):
    D,d,p,q=map(int,input().split())
    y=D%d
    c=y*(p+q*(D//d))
    x=d*(func(D,d,p,q))+c
    print(x)