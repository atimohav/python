def declen(x):
    for i in range(1,10):
        if x<10**i:
            return i

arr=[]

n,k=map(int,input().split())
nums=list(map(int,input().split()))

for i in range(n):
    for j in range(declen(nums[i])):
        arr.append((9-(nums[i]//(10**(j)))%10)*(10**j))
arr.sort(reverse=True)
k=min(k,len(arr))
print(sum(arr[0:k]))

