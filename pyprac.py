#print("Hello Luffy")
name= input("what's your name? ")
L = len(name)
if L<5 :
    print(f"cool name")
else:
    print(f"quite a name")
    
age = int(input('From when are you with dadan in years?  '))

print (f"you are in Pune from {int(age)}")
Totalage = int ( age + 3 )
print (f"ok, so.. {name} your age is {Totalage}")

num= Totalage % 2
print (num)
if num == 0 :
    print(f"is even")
else:
    print(f"is odd")

Name = name.upper()
print (f"Thanks {Name} ") 
'''for n in range (age):
    print (n)

d=0
while d<=10:
    print (d)
    d= d+1
'''

