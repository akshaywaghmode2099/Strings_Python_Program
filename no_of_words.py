'''Accept string from user and no of words in a string

i/p Hi hello bye
o/p no of words 3'''

str=input("Enter String ")
cnt=0
for ch in str:
    if ch==' ':
        cnt=cnt+1

print("No of words ",cnt+1)
