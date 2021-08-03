import re
mac="55:C8:99:66:77:11"
X = '([a-fA-F0-9]{2}[:]?){6}'

a=re.compile(X).search(mac)
if a:
     print("Its a match")
else:
     print("Its not a match")
