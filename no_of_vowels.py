'''Accept string from user and count no of vowels in it

i/p HI Hello Bye
o/p No of vowels 4'''

s=input("enter the string = ")
cnt=0
for ch in s:
    if ch in 'AEIOUaeiou':
        cnt=cnt+1

print("no of vowels ",cnt)
