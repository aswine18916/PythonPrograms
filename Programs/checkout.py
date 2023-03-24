def count_integers(a,b,c):
  if a!=b and b!=c:
    return 0
  if a==b and b==c:
    return 3
  else:
    return 2
print(count_integers(5,1,1))