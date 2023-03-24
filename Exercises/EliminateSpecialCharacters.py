import re
"""
Clearing the special characters in a sentence and printing
"""
input= "India is my country, all Indians are my brothers and sisters. I love my country"
s = input.lower()
s = ''.join(filter(str.isalnum, s))

print(s)



""









