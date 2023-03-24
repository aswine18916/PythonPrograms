s="XXV"
def roman_t0_integer(s):
    rom={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000,
    }
    res=0
    for i in range(len(s)):
        if i+1<len(s) and rom[s[i]]<rom[s[i+1]]:
            res=res-rom[s[i]]
        else:
            res=res+rom[s[i]]
    return res