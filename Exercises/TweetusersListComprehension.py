def count(n):
    if n>3:
        return
    print(n)
    count(n+1)
    print(n)
count(8)

# def sum(a,b):
#     s=a+b
#     return s
#
# print(sum(5,6))
# print(sum.__name__)


#
#
# a=[2,4,6,8,10,12]
# count=0
# for i in a:
#     if i!=a[-1]:
#         if i + (i+2) == 2* (i+1):
#             count=count+1
# print(count)


users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]
inactive_users=print(list(map(lambda x:x["username"].upper(),
                    filter(lambda a:not a['tweets'], users))))