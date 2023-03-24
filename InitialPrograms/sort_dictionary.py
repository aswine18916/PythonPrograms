dict={
    "aswin" : 34,
    "nikhila": 29,
    "anishk": 4
}

print(sorted(dict.items(), key=lambda x:x[1], reverse=True))