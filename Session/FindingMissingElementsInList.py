inp=[1,2,3,4,7,8,10]
def findmissing(lst):
    s=lst[0]
    e=lst[-1]
    return(sorted(set(range(s,e,1)).difference(lst)))

print(findmissing(inp))