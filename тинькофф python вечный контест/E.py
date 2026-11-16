def good_nums(l,r):
    res=0
    for i in range(1,19):
        for j in range(1,10):
            num=int(str(j)*i)
            if l<=num and num<=r:
                res+=1
    return res
    
l,r=map(int,input().split())
print(good_nums(l,r))
