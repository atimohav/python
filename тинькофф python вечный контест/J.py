def S(p):
    if len(p)<3:
        return 0
    if len(p)==3:
        return 1/2*abs((p[0][0]-p[2][0])*(p[1][1]-p[2][1])-(p[1][0]-p[2][0])*(p[0][1]-p[2][1]))
    res=0
    for i in range(1,len(p)-1):
        res+=S([p[0],p[i],p[i+1]])
    return res

def S_split(p, x):
    a,b=[x,None],[x,None]
    ai,bi=-1,-1
    for i in range(len(p)):
        if (p[i-1][0]<=x and x<p[i][0]) or (p[i][0]<x and x<=p[i-1][0]):
            x1,x2=p[i-1][0],p[i][0]
            y1,y2=p[i-1][1],p[i][1]
            y=(x-x1)*(y2-y1)/(x2-x1)+y1
            if a[1]==None:
                a[1]=y
                ai=i
            else:
                b[1]=y
                bi=i
    if b[1]==None:
        b[1]=a[1]
    p1=[a]
    p2=[b]
    flag=0
    for i in range(ai, ai+len(p)):
        ind=i%len(p)
        if flag==0 and ind==bi:
            flag=1
        if flag==0:
            p1.append(p[ind])
        else:
            p2.append(p[ind])
    p1.append(b)
    p2.append(a)
    return p1,p2

        
n=int(input())
p=[[0,0] for _ in range(n)]
minx=None
maxx=None
for i in range(n):
    p[i]=list(map(int,input().split()))
    if minx==None:
        minx=p[i][0]
    else:
        if minx>p[i][0]:
            minx=p[i][0]
    if maxx==None:
        maxx=p[i][0]
    else:
        if maxx<p[i][0]:
            maxx=p[i][0]

if n==1:
    print(minx)
elif n==2:
    print((maxx+minx)/2)
else:
    l=minx
    r=maxx
    while (r-l)>10**(-8):
        m=(l+r)/2
        p1,p2=S_split(p,m)
        ls,rs=0,0
        if p1[1][0]<=m and m<=p2[1][0]:
            lS=S(p1)
            rS=S(p2)
        else:
            lS=S(p2)
            rS=S(p1)
        if lS<=rS:
            l=m
        else:
            r=m
        
    print(l)






