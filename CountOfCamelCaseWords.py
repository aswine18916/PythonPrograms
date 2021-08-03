import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
s="saveChangesInTheEditor"
def camelcase(s):
    # Write your code here
    newstring=""
    final=""
    for c in s[1:]:
        if c.isupper():
            c=" "+c
        newstring=newstring+c
    final=s[0]+newstring
    print(final)
    final=final.split(" ")
    print(final)
    result=len(final)
    print(result)
camelcase(s)