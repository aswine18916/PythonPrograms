par=")))()(()()()()())(()()()())()()(("
c=0
i=0
par=list(par)
for each in par:
    if par[-1]=='(':
        par.pop(-1)
        c=c+1
    else:
        break
    if par[0]==')':
        par.pop(0)
        c=c+1
    else:
        break
print(c)
while i<(len(par)-1):
    if par[i] == par[i+1]:
        c = c + 1
    i=i+1
print(par)