import time

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
ts=time.time()+0

res=0
for i in range(l, r+1):
    res+=bin_pow(i, p-2, p)
print(res%p)
print(time.time()-ts)
'''
import time

import sys
from array import array

def solve():
    l,r,p=map(int,input().split())
    ts=time.time()+0
    
    n = r - l + 1
    
    # Используем array('I') для хранения 4-байтовых беззнаковых целых.
    # Это займет ~80 МБ вместо ~700 МБ у обычного списка list.
    pref = array('I', [0]) * n
    
    # 1. Считаем префиксные произведения
    curr = l % p
    pref[0] = curr
    for i in range(1, n):
        curr = (curr * (l + i)) % p
        pref[i] = curr
        
    # 2. Находим обратный элемент ко всему произведению за O(log p)
    inv_prod = pow(curr, p - 2, p)
    total_sum = 0
    
    # 3. Идем с конца, восстанавливая обратные элементы и сразу суммируя их
    x = r
    for i in range(n - 1, 0, -1):
        inv_x = (inv_prod * pref[i - 1]) % p
        total_sum += inv_x
        if total_sum >= p:
            total_sum -= p
            
        inv_prod = (inv_prod * x) % p
        x -= 1
        
    # 4. Добавляем обратный элемент для l
    total_sum = (total_sum + inv_prod) % p
    
    print(total_sum)
    print(time.time()-ts)

if __name__ == '__main__':
    solve()
'''

