l=[int(x) for x in input().split()][:n]
x=len(l)//2
z=l[:x]
z.sort()
c=l[x:a]
c.sort()
v=z+c
v.sort()
print(*v)

