# Calender
import calendar  
print("")
print(calendar.month(2020,5))
print("")

# if shortcut
a,b=10,3
max=a if a>b else b
print(max)
print("")
print(a if a<b else b)

# swap shortcut
print("")
a,b=2,4
b,a=a,b
print(a,b)

# list print with indexing using fromat method and enumerate
print("")
list=['sachin','rahul','kumar','rohit']
for i,n in enumerate(list,start=0):
    print(f'{i} -> {n}')

# two list zip
print("")
name=['ram','lakhan','vijay']
city=['mumbai','surat','bhavnagar']
for i,n in zip(name,city):
    print(f'{i} live in {n}')

# first value print in tuple
print("")
a,*_=(12,34,54,23)
print(a)

# first and last value print in tuple
print("")
a,*_,b=(12,34,54,23)
print(a,b)
print("")

# input password is hide (not showing) using getpass function
from getpass import getpass
Gmail = input("Enter the Email : ")
print("")
Password=getpass("Enter the Password")
print("")
print("Done!")

# print readable big numbers
print("")
n1=100_000_000
n2=100_000_0
s=n1+n2
print(f'{s:,}')

# open the file without close function
print("")
with open('Python_DB_conn.py') as f:
    print(f.read())

# print the random number using random function
print("")
import random
name ='askdjakjfadsads'
print(random.choice(name))