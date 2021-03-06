import re
"""
Clearing the special characters in a sentence and printing
"""
input= "India is my country, all Indians are my brothers and sisters. I love my country"
clean= re.sub("[*.,]", '', input)
print(clean)













