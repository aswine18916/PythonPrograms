"""Navigating to a  specific item in a dictionary"""
dict = {
  "Science": 10,
  "Commerce": 13,
  "Maths": 18,
  "English": 20,
  "Hindi": 25,
  "Sanskrit": 29
}

for k,v in dict.items():
    if v>12:
        print(k)