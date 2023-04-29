'''Accept complete name from user and print in format
lastname firstname middle name
i/p kavya ramdas Biradar
o/p Biradar Kavya Ramdas'''

str=input("Enter complete string ")
str=str.title()
s=(str.find(' '))
e=(str.rfind(' '))

fnm=str[e+1: ]+" "+str[:s]+" "+str[s+1:e]
print("formated name ",fnm)
