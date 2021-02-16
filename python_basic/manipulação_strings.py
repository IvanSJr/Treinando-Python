'''
upper()
lower()
len()
replace('str')
count('str')
find('str')
title()
'''

str = "aaaaaaaaaaaaa"
str = str.upper()
print(str)

str = "AAAAAAAAAAAAA"
str = str.lower()
print(str)

str = "AAAAAAAAAAAA"
print(len(str))

str = "Ivan Júnior"
str = str.replace("Júnior", "Santos")

str = "Ivan Santos de Jesus Júnior aaaaaaaa"
print(str.count("a")) #conta quantas tem

str = "A B C D E F G H I J K L"
print(str.find("J")) #procura onde está

str = "ivan santos de jesus junior"
str = str.title()
print(str)