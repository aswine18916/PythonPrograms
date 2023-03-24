words=["Four", "two", "three", "three", "two"]

def new_func(words):
    freq={}
    for each in words:
        if each not in freq:
            freq[each]=1
        else:
            freq[each]+=1

    print(freq)

new_func(words)

