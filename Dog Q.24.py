

a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
p={}
val=0
for x in a:
    if x['item']not in p:
        p[x['item']] = x['amount']
    else:
        p[x['item']]+=x['amount']
print(p)

# output={'item1':1150,'item2':300}
