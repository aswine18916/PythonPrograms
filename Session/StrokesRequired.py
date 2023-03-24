inp=["aaba", "aaca", "aabb"]


def StrokestoRequired(inp):
    i=int()
    j=int()
    visit='x'
    combination = 0
    update = []


    for word in inp:
        newlist=list(word)
        update.append(newlist)


    def traverse(update, i,j, checkchar):
        def validity(i, j, update, checkchar):
            r = len(update)
            c = len(update[0])
            if (i < 0 or j < 0 or i >= r or j >= c or update[i][j] != checkchar):
                return False
            else:
                return True
        update[i][j]=visit
        lisi=[0,1,-1,0]
        lisj=[1,0,0,-1]
        for k in range(len(lisi)):
            if(validity(i+lisi[k], j+lisj[k], update, checkchar)):
                traverse(update,i+lisi[k], j+lisj[k], checkchar)

    r = len(update)
    c = len(update[0])
    for i in range(r):
        for j in range(c):
            if update[i][j]!= visit:
                combination=combination+1
                traverse(update,i,j,update[i][j])
    return combination
    #print(combination)

kk=StrokestoRequired(inp)
print(str(kk))