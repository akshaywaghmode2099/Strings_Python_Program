s=input("Enter string ")
rev=s[::-1]
'''for i in range(-1,-len(s)-1,-1):
    rev=rev+s[i]
'''
if rev==s:
    print("It is palindrome")
else:
    print("It is not palindrome")
