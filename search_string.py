str=input("Enter string ")
sr=input("Enter search string ")
str=str.lower()
sr=sr.lower()
if str.count(sr)>0:
    print("String found ")
else:
    print("Not Found ")

