import re
def cumle_olustur(text):
    """
    parametre:  Cümlelere ayrılacak yazı.(str)
    return:     Cümlelere ayrılmış liste.(list)
    """
    sentences = re.split(r' (?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)', text)

    cumle_listesi = []

    counter = 0
    for stuff in sentences:
        x = stuff.split(".")
        for i in x:
            temp_str = (str(x[counter])+".") 
            temp_str = temp_str.strip()
            cumle_listesi.append(temp_str)
            counter = counter + 1 

    cumle_listesi.pop() # cumle_listesi listenin son elemanı '.' olarak kaldığından son elemanı siliyorum.

    return cumle_listesi


