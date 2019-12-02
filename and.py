n = int(input())
L = [int(x) for x in input().split()]
res = L[0]
for i in range(1,n) :
    res = res & L[i]
print(res,end='')
