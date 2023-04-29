'''Accept String from user and interchange first and last character
i/p Hello
o/p oellH'''

s=input("Enter string ")
s=s[-1]+s[1:-1]+s[0]
print("After interchanging first and last characters ",s)
