kelime = "gittimi"
def bol(kelime,key):
    
    lis=kelime.split(key)
    if("" in lis):
        lis.remove("")
    
    return lis

kelime = bol(kelime,"mi")
print(kelime)