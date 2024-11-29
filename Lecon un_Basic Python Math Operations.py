print("Leco un")
print ("Introductions and Basics\n")
print ("Welcome to Python\n")
print ("Always use or press Ctrl + / (Windows) to comment or comment out a block or selected lines wink wink\n")
#ctrl +s - to save
#ctrl +b - excecute

#Variables Declaration; start with lower case
f_num = 23
s_num = 20
addition = f_num + s_num
print (addition,"\n")

#To check data types use types
print (type(f_num), type(s_num), "\n")

#To  check memory Location use id
print (id(f_num), id(s_num), "\n")

#Data types
#1. int
num1 = 100
print(type(num1), "\n")

#2. float
num2 = 13.32
print(type(num2), "\n")

#3. string
s = "'Code' mtu wangu"
print (s, type(s), "\n")

#4. List
#k = (2,2,3,4,56)
i = (10, "kibe", 10, 20, "Welcome, \n")
print(i, "\n")
my_list=list(i)
my_list.append(0.8)
i=tuple(my_list)
print(i, "\n")

#5. $ tuple once defined cannot be changed
#$ =(2,2,23)

#6. Dict
D ={"name":"Kibe", "email":"kibe@gmail.com"}
print (D, "\n")

#7. Set can be updated added {}
s= {9,0,4,5}
print (s, "\n") 

#bool
bool: True or False
print (bool, "\n")

#9. complex : 4 +3j
#help(str)

#Operators

#1. Arithmetic operators +,-,*,/,//,remainder %,power of i.e ^3 ^4of **
n1=10
n2=3
n3=4

print(n1/n2, "\n") #results plus remainder
print(n1//n2, "\n") #results minus remainder
print(n1%n2, "\n") #gives remainder only
print(n1 ** n3, "\n") #power of^3 of

#2. Comparison Operator (bool) gives True or False<,>,<=,>=,==,!=

n1=120
n2=300
print(n1==n2, "\n")
print(n1>n2, "\n")

#3. Identity Operators is , isnot it checks at memory location
n1=100
n2=200
print(n1 is n2, "\n", "\n")
print(n1 is not n2, "\n")

l = {3,4,5}
l2 = (3,4,5)
print(l is l2, "\n") #is not, because lists allocates different memory location of both l and l2

#4 Assignment operators = , +=, -=, *=, /=
n1=100
n1 = n1 +5 # here we are increamenting  n1 to =5
print(n1, "\n")
n1 =n1 -4
print(n1, "\n")
n1+=5
print(n1, "\n")
n1-=5
print(n1, "\n")

#5 Bitwise Operators &,|,^,>>,<<
n1=2
n2=1
print(bin(n1),bin(n2), "\n") #binary representation of

#6. Logical Operators and,or, nor
print(10==10 and 20==20, "\n") #if both are right then true
print(10==15 or 20==20, "\n") #or asks for either
print(not(110==110), "\n")

#7. membership operators in,not in
l={10,20,30,40,50}
print(60 in l, "\n") #checking if an item is in the list
l= ("kibe is python is string")
print("kibe" in l, "\n")

print ("samuel" not in l, "kibe" not in l, "\n")






