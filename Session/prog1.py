# words=["one", "two", "three", "three", "two"]
# uniquewords=[]
# for word in words:
#     if word not in uniquewords:
#         uniquewords.append(word)
# print(uniquewords)


arr = ['one', 'one', 'two', 'three', 'three', 'two']
new=set(arr)
print(new)

# def yourfunction(words):
#     freq={}
#     for word in words:
#         if word not in freq:
#             freq[word]=1
#         else:
#             freq[word]+=1
#     return freq
#
# for k,v in yourfunction(arr).items():
#     v=str(v)
# print(yourfunction(arr))
#
# x='\n'.join(':'.join((str(k),str(v))) for (k,v) in yourfunction(arr).items())
# print(x)