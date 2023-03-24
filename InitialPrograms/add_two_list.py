A=[1]
B=[11,2,3]


def merge_lists(list1, list2):
    final = []
    empty=[]
    if len(list1) == len(list2):
        for i in range(len(list1)):
            final.append(list1[i])
            final.append(list2[i])
        print(final)
    elif len(list1) > len(list2):
        for i in range(len(list2)):
            final.append(list1[i])
            final.append(list2[i])
        for j in range(len(list2), len(list1)):
            final.append(list1[j])
        print(final)
    elif len(list2) > len(list1):
        for i in range(len(list1)):
            final.append(list1[i])
            final.append(list2[i])
        for j in range(len(list1), len(list2)):
            final.append(list2[j])
        return final
    else:
        return empty


merge_lists(A,B)