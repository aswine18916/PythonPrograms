sentence = "malayalam"
# print("Logic 1")
# """Logic 1"""
# final=""
# all_freq = {}
#
# for i in sentence:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1
#
# for k,v in all_freq.items():
#     print("The count of {} is {}".format(k,v))
#
# x='\n'.join(':'.join((str(k),str(v))) for (k,v) in all_freq.items())
# print(x)

print(list(set(sentence)))

"""Logic 2"""
print("Logic 2")
# new=[]
# for c in sentence:
#     if c not in new:
#         new.append(c)
# #print(new)
# for c in new:
#     print("The count of", c, "is ", sentence.count(c))

