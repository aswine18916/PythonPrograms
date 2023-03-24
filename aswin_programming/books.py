import re


def book_functions():
    filename = input("Please enter the filename : ")
    word=input("please enter the word you want to search : ")
    c=0
    pathfile="../aswin_programming/books/"+filename+".txt"
    with open (pathfile) as currentbook:
        entirebook=currentbook.readlines()
        readbookbyline=dict(enumerate(entirebook,start=1))
        for k,v in readbookbyline.items():
            if word in v:
                print(k, ".", v)
                c=c+1
            else:
                continue








book_functions()