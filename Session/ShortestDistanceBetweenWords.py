inputlist = ["My", "Name", "is", "Aswin", "Name","My", "QA", "Engineer", "is", "My", "Engineer"]

def distance(inputlist,word1,word2):
    new_list=[]
    word1_index=[]
    word2_index=[]
    enum=dict(enumerate(inputlist))
    print(enum)
    for k,v in enum.items():
        if v==word1:
            word1_index.append(k)
    for k, v in enum.items():
        if v == word2:
            word2_index.append(k)

    print(word1_index)
    print(word2_index)
    for i in word1_index:
        for j in word2_index:
            new_list.append(abs(i-j))
    print(new_list)
    print("largest distance is :" ,max(new_list)-1)
    print("smallest distance is :" ,min(new_list)-1 )


distance(inputlist, "Name", "My")