n,k = input().split()
n=int(n)
k=int(k)
a =list(map(int,input().split()))
b=list(map(int,input().split()))
bi=[]
for i in b:
    a.append(i)
    bi.append(max(a))
print(*bi)
