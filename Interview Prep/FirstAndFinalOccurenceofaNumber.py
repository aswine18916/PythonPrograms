listA=[1,5,3,4,6,5,7,5,8,5]
new=[]
dict_enum=dict(enumerate(listA))
print(dict_enum)
for k,v in dict_enum.items():
    if v==5:
        new.append(k)

print("max is {}, min is {}".format(max(new),min(new)))

