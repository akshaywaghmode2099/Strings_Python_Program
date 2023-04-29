'''Accept string from user and display alternate charaters

i/p : python
o/p  :pto'''

s=input("Enter string ")

'''for i in range(0,len(s)-1):
    if i%2==0:
        print(s[i],end="")
'''

for i in range(0,len(s)-1,2):
    print(s[i],end="")
