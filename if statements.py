#if statements 
#1 program that checks if a number is odd or even
x=int(input("enter"))
if x%2==0:
    print("it is an even no.")
else:
    print("it is an odd number")

#2 input 3 numbers out of which print the largest one
x=int(input("enter"))
y=int(input("enter"))
z=int(input("enter"))
max=x
if y>max:
    max=y
if z>max:
    max=z
print(max)

#3 program to test the divisibility of a no. with another number
x=int(input("enter"))
y=int(input("enter"))
print(x)
print(y)
if x%y==0:
    print("x is divisible by y")
else:
    print("not divisible")
    exit()

#4 program to display a menu for calculating area and perimeter of a circle
import math
r=float(input("enter"))
print("area")
print("perimeter")
x=input("choose 1 or 2")
if x=="1":
    s=(math.pi*r**2)
    print(s)
if x=="2":
    q=(2*math.pi*r)
    print(q)
else:
    print("choose 1 or 2")

#5 program to print whether a given character is an uppercase or a lowercaseor a digit or any other character
x=input("enter")
if x>="A" or x<="Z":
    print("u have entered an uppercase")
if x>="a" or x<="z":
    print("u have entered an lowercase")
if x>="0" or x<="9":
    print("u have entered a digit")
else:
    print("u have a special character")

#6 print the table of 3
num=3
for a in range(1,11):
    (num,"x",a,"=",num*a)

#7 program to calculate the factorial of a no.
num=int(input("enter"))
fact=1
a=1
while a<=num:
    fact*=a
    a+=1
print("the factorial is",num,"is",fact)

