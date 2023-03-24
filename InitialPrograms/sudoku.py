sud=[
[4,3,5,2,6,9,7,8,1],
[6,8,2,5,7,1,4,9,3],
[1,9,7,8,3,4,5,6,2],
[8,2,6,1,9,5,3,4,7],
[3,7,4,6,8,2,9,1,5],
[9,5,1,7,2,3,6,2,8],
[5,1,9,3,2,6,8,7,4],
[2,4,8,9,5,7,1,3,6],
[7,6,3,4,1,8,2,5,9],
]



def first_check(sud):
    for each in sud:
        for i in each:
            if i in range(1,10) and each.count(i)!=1:
                return False
                break
            else:
                continue
        return True

def second_check(sud):
    for k in range(9):
        for each in sud:
            if each[k] in range(1,10) and each.count(each[k])!=1:
                return False
                break
            else:
                continue
    return True


def third_check(sud):
    final=[]
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            temp = []
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    if sud[r][c] != 0:
                        temp.append(sud[r][c])
            final.append(temp)
    for every in final:
        for item in every:
            if item in range(1, 10) and every.count(item) != 1:
                return False
                break
            else:
                continue
        return True
res1=print(first_check(sud))
res2= print(second_check(sud))
res3= print(third_check(sud))


if first_check(sud) and second_check(sud) and third_check(sud):
    print("valid sudoku")
else:
    print("invalid")