'''Accept string from user and also accept search string
from user if search string present then print it's total occurance
otherwise  display error message

i/p I like all programming language
search: a
o/p a present 4 times
search : java
o/p java is not found in a string '''
'''
str=input("Enter string ")
sr=input("Enter search string ")

ans=str.count(sr)
if ans>0:
    print(sr," is present ",ans," times")
else:
    print(sr," not found")
'''

str=input("Enter a string")
find= input("Enter a search string")
a=(str.count(find))
if a==0:
    print("not found ")
else:
    print(find,"present",a,"times")













    
