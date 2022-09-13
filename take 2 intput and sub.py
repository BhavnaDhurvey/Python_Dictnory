a={'shopping list':{'apple':9,'mango':10,'cherry':11}}
b=input("enter the number...")
c=int(input("enter the number..."))
for x in a:
    for k in a[x]:
        s=x,k
        d=a[k]-c     
print(s)
print(d)