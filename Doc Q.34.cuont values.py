dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# d=dict.values()
# print(d)
count=0
for key,value in dict.items():
    if value in dict:
        print(value)


# count = 0
# # using .items()
# for key, value in dict.items():
#    if isinstance(value, list):
#       count += len(value)
# print("The number of elements in lists: \n",count)