#1. Python data types - Strings, Lists, Tuple, Dictionaries
#string

#Indexing
s = "hellow World, bonjour le monde"
print(s[2]) #count from far right
print(s[-2])  #count from far left

# Slicing
print(s[0:5]) #start 0 to end 5
print(s[7:])  #start from 7
print(s[:6])  #end at 6 from default 0

#Stride
print(s[::3])  #no start no end but print 2nd characters at string -from right
print(s[::-2]) #from left


for value in s:
	print(value, "\n")

 #2. Built in functions
 #help(str)
 #print(dir(str))
 #format
n1 = 100
n2 = 200
print("Value of n1 is {}, Value of n2 is {}".format(n1,n2), "\n")
print("Value of n1 is {val1}, Value of n2 is {val2}".format(val1=n1,val2=n2), "\n")

s = s.capitalize()
print(s)


# upper
# lower
# title
print(s.upper())
print(s.lower())
print(s.title()) #capitalize first letter of word in str

# isupper
# islower
# istitle return true or false

print(s.istitle(), "\n") #etc

#split
#join

s1 = "HTML,CSS,Python,JAVA,C++,HTML"
l = s1.split(",")
print(l)

s2=(" ").join(l)
print(s2, "\n")

s4="abcd"
s5="1234"
s6="Python sample sample string abcd"

# maketrans
# translate

table = str.maketrans(s4,s5)
result = s6.translate(table)
print(result, "\n")

# index
# find
# rfind function

print("sample" in s6)
print(s6.index("sample")) #index of s in sample at - string
print(s6.find("sample")) #if simple was not there results is -1
print(s6.rfind("sample"), "\n") #checks the last sample in string


s7="***This is a sample string***"
s8= s7.strip("*") 
print(s8)
s8= s7.lstrip("*") # remove space or * from left side
print(s8)
s8= s7.rstrip("*") # remove space or * from right side
print(s8, "\n")

s9= "Python"
s10=s9.center(10,"1") #center string then add items on both sides
print(s10)

s11=s9.rjust(10,"1") #add item on the right of a string
print(s11)
s12=s9.ljust(10,"1") ##add item on the left of a string
print(s12, "\n")

s13=s1.replace("HTML", "HTML5")
print(s13, "\n")

#LIST
#are mutable aad,update and delete
#ordered data type indexing and slicing
# heterogenous datatype
l = [10,20,30,40,"Python", "JAVA", [100,200,300]]
print(l,type(l))

# Indexing and slicing
print(l[-1][1])
print(l[::-1])  #reverse

l1 = [100,200,300,400]
for value in l1:
	print(value, "\n")

for value in l1[::2]: #every seconnd number
	print(value)

#append
print(id(l1))
l1.append(500)
l1.append([501,502,503])
print(l1,id(l1))

#extend
l1.extend([600,700,701])
print(l1)

# l1.extend("python")
# print(l1)

#insert
l1.insert(1,150)
print(l1, "\n")

l2 = [10,20,30]
l3 = l2 
print(id(l2),id(l3))
print(l2,l3)
l2.append(40)
print(l2,l3)

l3 = l2.copy()
print(l2,l3)
l2.append(46)
print(l2,l3,"\n")

# update
l4 = [1,2,3,4,5]
l4[2] = 3.1
print(l4)

# delete pop,remove, clear, del
p = l4.pop()
print(l4,p)
p = l4.pop(1)
print(l4,p)

l4.remove(4)
print(l4)

l4.clear()
print(l4, "\n")

# del l4

l5 = [50,40,30,20,10]
l5.sort()
print(l5)
l5.reverse()
# print(l5[::-1])
print(l5)

# or
l6 = sorted(l5)
print(l6)

print(l5.index(40))
print(l5.count(40))

print(l5+l6,"\n")

l7=[0.1]
print(l7*10, "\n")

# tuple have parethesis
# immutable no adding,deleting ot updating
# ordered structure supports indexing and slicing
t = (10,20,20,20,30,40)
print(t,type(t))
# indexing , if multiple value os same length indexing return the index of the first value ignores the rest
print(t[0])
print(t.index(20))
print(t.count(20))
# slicing
print(t[:3])

t1= list(t) #also tback to tuple
print(t1, type(t1))
t2 = tuple(t1)
print(t2, type(t2),"\n")

# Disctionaries
# mutable
# unordered
# key shoud be unique no duplicates
# keys should be immutable. int,float,str,tuple add,update,delete

d= {"emp_id":101,"name":"abc", "email":"abc.gmail.com"}
print(d)

d["contact_no"] = 1212 #add 
print(d)

d["contact_no"] = 1222 #upade since can not duplicate
print(d)
print(d["email"]) #find item
print(d.get("name"))
print(d.get("age")) #key doesn't exist
print(d.setdefault("age")) ##checks if it key exists if doesn't, sets a default none
print(d.setdefault("Salary",100000)) #checks if it exists if doesn't, sets a default
print(d, "\n")

# iterate
for x in d:
	print(x, "\n")

for key in d:
	print(key,d[key])

# keys
# values
# items
print(d.keys(),"\n")
print(d.values(),"\n" )
print(d.items())
for t in d.items():
	print(t, "\n")

d1 = {}
for value in range(1,11):
	d1[value] = value*value
print(d1)

l8 = [1,2,3,4,5]
l9 = [1,4,9,16,25]
d2 = dict(zip(l8,l9))
print(d2)

l10 = [1,2,3,4,5]
d3 = dict.fromkeys(l10)
print(d3)
d3 = dict.fromkeys(l10,0)
print(d3, "\n")

# upade dictionary
d4 = {1:1,2:4,3:9,4:16}
d5 = {5:25,6:36,7:49}
#d4.update(d5)
#print(d4)

#Delete pop,popitem,clear, del
print(d4)
r = d4.pop(2) #pops only key
print(d4,r)
r = d4.popitem() #takes no arguments #pops key and value
print(d4, r)

d4.clear()
print(d4, "\n")

# del d4
# print(d4) #throws an error since it has deleted the whole dictionary.

# Set data tpyes: 
# add - update - delete
# mutable
# all elements should be unique
# immutable elements in the set - int, floattuple str
# unordered -no indxing or slicing

st = {10,20,30,40,100,200}
print(st,type(st))

# add
st1 = {100,200,300,400}
st1.add(500)
print(st1)

# union intersection unique elements
st2 = st.union(st1)
print(st2)

# intersection - common elements in the set
st3 = st.intersection(st1)
print(st3)

# Different operation - elements in set one not in set two and vise versa
st4 = st.difference(st1)
print(st4)

st4 = st1.difference(st)
print(st4)

# symmetric difference - common elements not part of the output
st5 = st.symmetric_difference(st1)
st4 = st.difference(st1)
print(st5)

# update
# print(st)
# st.update(st1)
# print(st)

# intersection update - common elements in both
# st.intersection_update(st1)
# print(st)

# difference update  elements in st not in st1
st.difference_update(st1)
print(st, "\n")

# st1.difference_update(st)
# print(st1)

# st.symmetric_difference_update(st1)
# print(st)

print(st1.issubset(st)) #is everything in st1 is in st?
print(st.issuperset(st1))

# typecasting -0 only unique elements

l11 = [100,200,300,400,500,400,500]
s = set(l11)
print(s, "\n")

l12 = [25,35,50,55,25,255,20,10,5]

s1 = set(l11)
s2 = set(l12)

s3 =s1.union(s2)
print(s3,type(s3))

# option one to sort: long process create a lsit then sort
# l13 = list(s3)
# print(l13)
# l13.sort()
# print(l13)

# option two use sorted
l13 = sorted(s3)
print(l13, "\n")

# delete option for set, pop,remove, discard, clear, del

s4 = {100,200,300,400,500,600}

r = s4.pop() #pops any of its liking
print(s4,r)

s4.remove(100) #removes item identified in argument, throws error if item is not in the list
print(s4)

s4.discard(200) #ensure there is an argument or you will haver an error - removes item identified however doesn't throw an error incase item is unavailable.
print(s4)

s4.clear()# to remove everything
print(s4, "\n")

# MATH AND RANDOM MODULE IN PYTHON
l14 = [100,20,300,400,500]
print(sum(l14)) #sum of list
print(max(l14)) #max of list
print(min(l14), "\n") #min of list

num= 25.65 
print(round(num,1), "\n") #to decimal places use round
# print(dir(__builtins__))
# help(__builtins__)

import math

l = [0.1] * 10
print(l)
print(sum(l))
print(math.fsum(l), "\n")

num1 = 15.559
print(math.floor(15.559),math.ceil(15.559))

# square
print(math.sqrt(25))
#factorial
print(math.factorial(5))

print(math.modf(num1))
d,i = math.modf(num1)
print(d)
print(i, "\n")

# 6 power of a number e.g 5^2
print(math.pow(10,2))
# logarithm
print(math.log(10,2)) #e.g log10base2
print(math.log(10)) #log10base (e)

print(math.log10(2)) #log2base10
print(math.log2(10)) #log10base2

print(math.sin(0))
print(math.sin(10)) #in degrees by default which gives a wrong answer
print(math.sin(math.radians(10))) #convert 30 to radiant then find its sin
print(math.cos(math.radians(10)))
print(math.tan(math.radians(10)),"\n")

# help(math)
# print(dir(math))

# generate random numbers
import random

print(random.random()) #always between 0-1

# DICE OF 6 NUMBERS
dice = [1,2,3,4,5,6]
print("Dice:", random.choice(dice))
# select random number from a SPECIFIC RANGE
print("Number is:", random.randint(10,100)) #gives even 100
print("Number is:", random.randrange(10,100)) #range gives upto 99
# float random number
print("Number is:", random.uniform(10,100))
