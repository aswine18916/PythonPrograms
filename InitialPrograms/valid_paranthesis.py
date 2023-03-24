s="([)}"
si="((((}}}}"

def check_valid_paranthesis(s):
    final = list(set(s))
    count_items = {}
    for each in final:
        count_items[each] = s.count(each)
    print(count_items)
    if len(s)==0:
        return False
    elif len(s)%2!=0:
        return False
    else:
        for each in count_items.keys():
            if "(" in count_items.keys() and ")" in count_items.keys():
                if count_items["("]>0 and count_items[")"]>0 and count_items["("]==count_items[")"]:
                    pass
                else:
                    return False
            if "{" in count_items.keys() and "}" in count_items.keys():
                if  count_items["{"]>0 and count_items["}"] and count_items["{"]==count_items["}"]:
                    pass
                else:
                    return False
            if "[" in count_items.keys() and "]" in count_items.keys():
                if  count_items["["]>0 and count_items[")"]>0 and count_items["["]==count_items["]"]:
                    pass
                else:
                    return False
            return True

print(check_valid_paranthesis(s))