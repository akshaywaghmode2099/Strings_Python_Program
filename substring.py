'''Accept string from user and also accept substring from user
and check given substring is present in string or not
 i/p i like java programmming
 search string java
 o/p java is found in string'''

s=input("Enter the String")
sb=input("Enter the Sub String")
if sb in s:
    print("Given ",sb," found in ",s)
else:
     print("Given ",sb," NOT found in ",s)
