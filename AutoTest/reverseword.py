String = "HelloWorld"
rev = ""
# str=String.split(" ")
# for st in str:
#     st=st[::-1]
#     rev=rev+" " +st
# print(rev)

for each in String:
    rev = each + rev
print(rev)
