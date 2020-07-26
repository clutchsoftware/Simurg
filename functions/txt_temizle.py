f = open("data/out_of_digits_dataset.txt", "r",encoding="utf-8")
f1 = open("data/out_of_dataset.txt", "w",encoding="utf-8")

"""
dosya oku ve bir karakteri silerek yeniden oluştur
örnek her kelimenin sonunda boşluk var silip yeniden yaz
bir karakter '\n' diğeri bosluk
"""

lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][0:len(lines[i])-2]
    f1.write(lines[i]+"\n")
