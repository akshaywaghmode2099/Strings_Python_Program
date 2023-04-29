'''Accept String (first name and last name) from user and
display in form of last_name first name
eg i/p Neha Biradar
o/p Biradar Neha'''

fn=input("Enter name ")
p=0;
for i in range(0,len(fn)):
    if fn[i]==" ":
        p=i
        break
print(fn[p+1:]+" "+fn[0:p])
