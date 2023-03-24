li=[[0,1,2],[3,4,5],[6,7,8]]
li2 = [ y for x in li for y in x]

print(','.join(map(str,li2)))