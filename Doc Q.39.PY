

marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
s={}
for (key, value) in marks.items():
    if value >= 170:
        s[key]=value
print(s)

# output={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}