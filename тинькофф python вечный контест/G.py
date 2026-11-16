n=int(input())
a=list(map(int,input().split()))
x,y=-1,-1
a_=[0]*len(a)
for i in range(n):
    a_[a[i]-1]+=1
k,l=-1,-1
for i in range(n):
    if a_[a[i]-1]==2:
        if k==-1:
            k=i+1
        else:
            l=i+1
for i in range(n):
    if a_[i]==0:
        y=i+1

ak=[0]*n
al=[0]*n
for i in range(n):
    ak[i]=a[i]
    al[i]=a[i]
ak[k-1]=y
al[l-1]=y

flag=True
ind=1
a_=[0]*n
for i in range(n):
    ind=ak[ind-1]
    a_[ind-1]+=1
    if a_[ind-1]>1:
        flag=False
        break
if flag:
    x=k

flag=True
ind=1
a_=[0]*n
for i in range(n):
    ind=al[ind-1]
    a_[ind-1]+=1
    if a_[ind-1]>1:
        flag=False
        break
if flag:
    x=l

if x!=-1 and y!=-1:
    print(x, y)
else:
    print(-1, -1)
