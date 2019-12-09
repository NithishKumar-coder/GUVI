s=[5,4,3,2,1]
w=len(s)
for i in range(1,w):
  for j in range(w):
    if s[i]<s[j]:
      s[i],s[j]=s[j],s[i]
print(*s)
