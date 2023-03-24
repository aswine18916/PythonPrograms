def check_min_char(str):
    if str==str[::-1]:
        print("its a palindrome")
    else:
        new=list(str)
        new.append(new[0])
        if new==new[::-1]:
            print("now its a palindrome after {} insertion".format(1))
            print("The string after adding character is -->", ''.join(new))
        else:
            for i in range(1,len(new)):
                new.insert(-int(i),new[i])
                if new == new[::-1]:
                    print("now its a palindrome after {} insertion".format(i+1))
                    print("The string after adding characters is -->",''.join(new))
                    break
                else:
                    continue



check_min_char("ABC")