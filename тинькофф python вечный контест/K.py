def bin_pow(x, y, p):
    x%=p
    y%=(p-1)
    if y==0:
        return 1
    if y==1:
        return x
    if y%2==0:
        return (bin_pow(x, y//2, p)**2)%p
    return ((bin_pow(x, y//2, p)**2)*x)%p

def power_mod(x, y, p):
  res = 1
  x = x % p
  while y > 0:
    if y % 2 == 1:
      res = (res * x) % p
    y = y // 2
    x = (x * x) % p
  return res


l,r,p=map(int,input().split())

res=0
for i in range(l, r+1):
    res+=bin_pow(i, p-2, p)
print(res%p)
