
Dic ={
    1:'NAVGURUKUL',
    2:'IN',
      3:{
      'A' : 'WELCOME',
      'B' : 'TO',
      'C' : 'DHARAMSALA'
    }
}
for i in Dic:
    del Dic[3]['A']
    break
print(Dic)


# s=3['A']
# d={}
# for key,value in Dic.items():
#     if key not in s:
#         d[key]=value
# print(d)


# Output :-
# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',
# 3:
# { 'B' : 'To',
# 'C' : 'DHARAMSALA'
# }
# 