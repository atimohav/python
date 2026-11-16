n=int(input())
h=list(map(int,input().split()))
i=-1
j=-1
pos=True
for k in range(n):
    if h[k]%2!=(k+1)%2:
        if h[k]%2==0:
            if i==-1:
                i=k+0
            else:
                pos=False
                break
        else:
            if j==-1:
                j=k+0
            else:
                pos=False
                break
            
if pos and i!=-1 and j!=-1:
    print(i+1,j+1)
elif pos and i==-1 and j==-1 and n>=3:
    print(1,3)
else:
    print(-1,-1)
