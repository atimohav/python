A,B,C,D = map(int, input().split())

if D<=B:
    print(A)
else:
    print(A+(D-B)*C)
