'''str="i Like Programming JAVA"
print(str.capitalize()) 
print(str.lower())
print(str.upper())
str="python123"
print(str)
print(str.isalnum())
str="Python"
print(str.isalpha())
str=" "
print(str.isspace())
print('p'.isalpha())
str='123'
print("Digit ",str.isdigit())
str='Python123'
print("Digit ",str.isdigit())
s="no_1"
print("identifier ",s.isidentifier())

str="I like java programming java"
print(str.index('i'))
print("java index ",str.index('java'))#3
print("i in index 10 ",str.index('i',10,len(str)))


print("last occurance ",str.rindex('i'))
print("last index of java",str.rindex('java'))
print("i in index 10 ",str.rindex('i',10,len(str)))
#print(str.index('z'))



str='nnnn'
print(str.find('n'))  #0
print(str.rfind('n')) #3
print(str.find('z'))  #-1

str="i Like Programming JAVA "
print(str.count("JAVA"))    #1
print(str.count("python"))  #0
print(str.count('i',0,6))   #2
print("swap case ",str.swapcase())


str="i Like Programming JAVA"
print("string starts with ",str.startswith('i'))
print("string starts with ",str.endswith('vA'))

str="hello"
print(str.rjust(10))        
print(str.rjust(10,'*'))
print(str.ljust(10,'$'))
print(str.center(10,'#'))

     hello
*****hello
hello$$$$$
##hello###

str="i like PYTHON"
print("capitalized ",str.capitalize())
print("title ",str.title())

str="     hello bye   hello    "
print(str.lstrip())
print(str.rstrip())
print(str.strip())
str="hhhhth bye zhhh hj......"
print(str.lstrip('h'))
print(str.rstrip('.'))

str="i like java php java programming java"
print(str)
print(str.replace('j','J'))

'''

str="123"
print(str)
print(str.rjust(10))
print(str.zfill(10))











































