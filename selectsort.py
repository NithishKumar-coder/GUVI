n=int(input())
l=[int(x) for x in input().split()][:n]
d=len(l)
for i in range(d):
  for j in range(i+1,d):
    if l[i]>l[j]:
      l[i],l[j]=l[j],l[i]
  print(l)
