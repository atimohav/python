def my_min(a,b):
    if a<0 and b<0:
        return -1
    if a<0:
        return b
    if b<0:
        return a
    if a>b:
        return b
    return a

n=int(input())
if n>0:
    p=[0]*n
    mt=0
    for i in range(n):
        p[i]=int(input())
        if p[i]>100:
            mt+=1

    s=[[-1]*(mt+1) for _ in range(n)]
    #s[i][j] i-индекс обеда, который мы купили на этом шаге, j-кол-во токенов после покупки этого обеда
    if p[0]>100:
        s[0][1]=p[0]
    else:
        s[0][0]=p[0]

    for i in range(1,n):
        for j in range(mt+1):
            a,b=-1,-1
            if p[i]>100:
                if j-1>=0:
                    if s[i-1][j-1]>=0:
                        a=s[i-1][j-1]+p[i]
            else:
                if s[i-1][j]>=0:
                    a=s[i-1][j]+p[i]
            if j+1<=mt:
                if s[i-1][j+1]>=0:
                    b=s[i-1][j+1]
            s[i][j]=my_min(a,b)
    print(min(filter(lambda x: x>=0, s[-1])))

else:
    print(0)
