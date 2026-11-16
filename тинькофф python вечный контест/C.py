n,t=map(int,input().split())
fl=list(map(int,input().split()))
bw=int(input())-1

if fl[bw]-t<=fl[0] or fl[bw]+t>=fl[-1]:
    print(fl[-1]-fl[0])
else:
    print(fl[-1]-fl[0]+min(fl[-1]-fl[bw],fl[bw]-fl[0]))


